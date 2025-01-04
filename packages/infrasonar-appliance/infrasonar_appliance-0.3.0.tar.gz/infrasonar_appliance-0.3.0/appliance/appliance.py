#!/usr/bin/env python
import os
import sys
import asyncio
import argparse
import textwrap
import signal
import re
import yaml
import string
from abc import abstractmethod
from configobj import ConfigObj
from enum import Enum
from typing import NamedTuple, Optional, Tuple, List, Any
import curses
import _curses
import functools
from setproctitle import setproctitle
from aiohttp import ClientSession


__version__ = '0.3.0'  # Update version in setup.py as well

_RE_DOCKER_VERSION = \
    re.compile(r'Docker version ([0-9]+)\.([0-9]+)\.([0-9]+).*')
_RE_COMPOSE_PATH = \
    re.compile(r'infrasonar\s+([a-z]+).*\s+(\/.*)docker-compose\.yml')
_RE_RUNNING_PROBE = \
    re.compile(r'^infrasonar-([a-z0-9_]+)-probe-1.*$')
_RE_COLOR = re.compile(r'\x1b\[[0-9][0-9]?m')
_MIN_DOCKER_VERSION = 24

_X_INFRASONAR_TEMPLATE = {
    'labels': {'com.centurylinklabs.watchtower.scope': '${AGENTCORE_TOKEN}'},
    'logging': {'options': {'max-size': '5m'}},
    'network_mode': 'host',
    'restart': 'always',
    'volumes': ['./data:/data/']
}

_SOCAT = {
    'image': 'alpine/socat',
    'command': 'tcp-l:443,fork,reuseaddr tcp:${SOCAT_TARGET_ADDR}:443',
    'expose': [443],
    'restart': 'always',
    'logging': {'options': {'max-size': '5m'}},
    'network_mode': 'host'
}

_WATCH_TOWER = {
    'environment': {
        'WATCHTOWER_CLEANUP': True,
        'WATCHTOWER_INCLUDE_RESTARTING': True,
        'WATCHTOWER_POLL_INTERVAL': 21600,
        'WATCHTOWER_SCOPE': '${AGENTCORE_TOKEN}'
    },
    'image': 'containrrr/watchtower',
    'volumes': [
        '/var/run/docker.sock:/var/run/docker.sock',
        '/etc/localtime:/etc/localtime:ro'
    ]
}

_AGENTCORE = {
    'environment': {
        'AGENTCORE_ZONE': '${AGENTCORE_ZONE_ID}',
        'HUB_HOST': '<HUB_HOST>',
        'TOKEN': '${AGENTCORE_TOKEN}'
    },
    'image': 'ghcr.io/infrasonar/agentcore'
}

_DOCKER_AGENT = {
    'environment': {
        'TOKEN': '${AGENT_TOKEN}',
        'API_URI': '<API_URL>'
    },
    'image': 'ghcr.io/infrasonar/docker-agent',
    'volumes': [
        '/var/run/docker.sock:/var/run/docker.sock',
        './data:/data/'
    ]
}

_SPEEDTEST_AGENT = {
    'environment': {
        'TOKEN': '${AGENT_TOKEN}',
        'API_URI': '<API_URL>'
    },
    'image': 'ghcr.io/infrasonar/speedtest-agent'
}

_AGENTS = {
    'docker': _DOCKER_AGENT,
    'speedtest': _SPEEDTEST_AGENT,
}

USE_DEVELOPMENT = 0


def get_rapp(compose_path: str, use_development: bool) -> dict:
    COMPOSE_FILE = \
        os.path.join(compose_path, 'docker-compose.yml')
    CONFIG_FILE = \
        os.path.join(compose_path, 'data', 'config', 'infrasonar.yaml')
    ENV_FILE = \
        os.path.join(compose_path, '.env')

    return {
        'image': 'ghcr.io/infrasonar/rapp',
        'environment': {
            'USE_DEVELOPMENT': use_development,
            'COMPOSE_FILE': COMPOSE_FILE,
            'CONFIG_FILE': CONFIG_FILE,
            'ENV_FILE': ENV_FILE,
        },
        'volumes': [
            f'{compose_path}:{compose_path}',
            '/var/run/docker.sock:/var/run/docker.sock'
        ],
    }


def eq(left, right):
    return left == right


def ne(left, right):
    return left != right


def read_docker_version(output):
    m = _RE_DOCKER_VERSION.match(output)
    if not m:
        return
    try:
        major, minor, patch = int(m.group(1)), int(m.group(2)), int(m.group(3))
    except Exception:
        return
    return major, minor, patch


PRINTABLE_CHARS = set([ord(c) for c in string.printable])
TOKEN_CHARS = set([ord(c) for c in '0123456789abcdef'])
SOCAT_TARGET_CHARS = set([ord(c) for c in (
    '.0123456789'
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ')])
TOKEN_LEN = 32


class DockerNotFound(Exception):
    install_url = 'https://docs.docker.com/compose/install/'


class DockerNoVersion(Exception):
    pass


class DockerVersionTooOld(Exception):
    pass


class InfraSonarNotRunning(Exception):
    pass


class InfraSonarNotFound(Exception):
    pass


class InfraSonarWrongEnv(Exception):
    pass


class Step(Enum):
    Init = 0
    Main = 1
    Apply = 2
    ManageProbes = 3
    Synchronize = 4
    ManageProbe = 5
    ManageAgents = 6
    Rapp = 7
    ViewLogs = 8
    Install = 9


class Part(Enum):
    Environment = 'environment'
    Config = 'config'


class State:
    loop: asyncio.AbstractEventLoop = asyncio.new_event_loop()
    probes_config_meta: Optional[dict] = None
    api_url: str
    hub_host: str
    step: Step = Step.Init
    status: Optional[str] = None
    compose_path: Optional[str] = None
    compose_data: Optional[dict] = None
    config_data: Optional[dict] = None
    agentcore_token: Optional[str] = None
    agent_token: Optional[str] = None
    agentcore_zone_id: Optional[int] = None
    socat_target_addr: Optional[str] = None
    container_id: Optional[int] = None
    has_changes: bool = False
    running_probes: set = set()

    @classmethod
    def get_probe_tag(cls, probe: str):
        pdata = cls.compose_data['services'].get(f'{probe}-probe', {})
        imagestr = pdata.get('image', '')
        if 'probe:' in imagestr:
            tag = imagestr.split('probe:')[1]
            return 'stable' if tag == 'latest' else tag
        return 'stable'

    @classmethod
    def headers(cls):
        return {'Authorization': f'Bearer {cls.agent_token}'}

    @classmethod
    async def read_container_id(cls):
        if cls.container_id is not None:
            return
        url = f'{State.api_url}/container/id'
        async with ClientSession(headers=cls.headers()) as session:
            async with session.get(url, ssl=True) as r:
                if r.status != 200:
                    msg = await r.text()
                    raise Exception(f'{msg} (error code: {r.status})')
                resp = await r.json()
                cls.container_id = resp['containerId']

    @classmethod
    async def refresh_enbled_probes(cls):
        await cls.read_container_id()
        params = 'fields=key,kind'
        url = f'{cls.api_url}/container/{cls.container_id}/collectors?{params}'
        async with ClientSession(headers=cls.headers()) as session:
            async with session.get(url, ssl=True) as r:
                if r.status != 200:
                    msg = await r.text()
                    raise Exception(f'{msg} (error code: {r.status})')
                resp = await r.json()
                probes = set(c['key'] for c in resp if c['kind'] == 'probe')
                current = set(cls.get_probes())
                for probe in current-probes:
                    del cls.compose_data['services'][f'{probe}-probe']
                    cls.has_changes = True
                for probe in probes-current:
                    p = cls.compose_data['x-infrasonar-template'].copy()
                    p['image'] = f'ghcr.io/infrasonar/{probe}-probe'
                    cls.compose_data['services'][f'{probe}-probe'] = p
                    cls.has_changes = True

    @classmethod
    async def read_running_probes(cls):
        cls.running_probes = set()
        try:
            cmd = 'docker compose ps'
            proc = await asyncio.create_subprocess_shell(
                cmd,
                stderr=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                cwd=State.compose_path,
            )

            stdout, stderr = await proc.communicate()
            out = stdout.decode()
            for line in out.splitlines():
                m = _RE_RUNNING_PROBE.match(line)
                if m:
                    cls.running_probes.add(m.group(1))
        except Exception:
            pass

    @classmethod
    def write(cls):
        try:
            fn = os.path.join(cls.compose_path, '.env')
            conf = ConfigObj()
            conf.filename = fn
            conf['AGENTCORE_TOKEN'] = cls.agentcore_token
            conf['AGENT_TOKEN'] = cls.agent_token
            conf['AGENTCORE_ZONE_ID'] = cls.agentcore_zone_id
            conf['SOCAT_TARGET_ADDR'] = cls.socat_target_addr or ''
            conf.write()
        except Exception as e:
            msg = str(e) or type(e).__name__
            raise Exception(f'failed to write {fn} ({msg})')

        try:
            fn = os.path.join(cls.compose_path, 'docker-compose.yml')
            with open(fn, 'w') as fp:
                fp.write(r"""
## InfraSonar docker-compose.yml file
##
## !! This file is managed by InfraSonar !!

""".lstrip())
                yaml.safe_dump(cls.compose_data, fp)
        except Exception as e:
            msg = str(e) or type(e).__name__
            raise Exception(f'failed to write {fn} ({msg})')

        try:
            fn = os.path.join(
                cls.compose_path,
                'data',
                'config',
                'infrasonar.yaml')
            with open(fn, 'w') as fp:
                fp.write(r"""
## WARNING: InfraSonar will make `password` and `secret` values unreadable but
## this must not be regarded as true encryption as the encryption key is
## publicly available.
##
## Example configuration for `myprobe` collector:
##
##  myprobe:
##    config:
##      username: alice
##      password: "secret password"
##    assets:
##    - id: [12345, 34567]
##      config:
##        username: bob
##        password: "my secret"
##
## !! This file is managed by InfraSonar !!
##
## It's okay to add custom probe configuration for when you want to
## specify the "_use" value for assets. The appliance toolktip will not
## overwrite these custom probe configurations. You can also add additional
## assets configurations for managed probes.

""".lstrip())
                yaml.safe_dump(cls.config_data, fp)
        except Exception as e:
            msg = str(e) or type(e).__name__
            raise Exception(f'failed to write {fn} ({msg})')

    @classmethod
    def read_infrasonar_status(cls, out: str):
        for line in out.splitlines():
            m = _RE_COMPOSE_PATH.match(line)
            if m:
                cls.status = m.group(1)
                cls.compose_path = m.group(2)
                break
        else:
            curdir = os.path.realpath(os.path.curdir)
            for p in (curdir, '/etc/infrasonar'):
                fn = os.path.join(p, 'docker-compose.yml')
                if os.path.exists(fn):
                    try:
                        with open(fn, 'r') as fp:
                            data = yaml.safe_load(fp)
                        assert data['services']['agentcore']
                        assert data['x-infrasonar-template']
                    except Exception:
                        pass
                    else:
                        cls.compose_path = os.path.abspath(p)
                        cls.status = 'not running'
                        break
                else:
                    cls.status = 'not found'
        if cls.compose_path:
            fn = os.path.join(cls.compose_path, 'docker-compose.yml')
            try:
                with open(fn, 'r') as fp:
                    compose_data = yaml.safe_load(fp)
            except Exception as e:
                msg = str(e) or type(e).__name__
                cls.status = f'broken compose file ({msg})'
                return
            else:
                cls.compose_data = compose_data
            fn = os.path.join(cls.compose_path, '.env')
            try:
                conf = ConfigObj(fn)
                cls.agentcore_token = conf['AGENTCORE_TOKEN']
                cls.agent_token = conf['AGENT_TOKEN']
                cls.agentcore_zone_id = int(conf.get('AGENTCORE_ZONE_ID', 0))
                cls.socat_target_addr = conf.get('SOCAT_TARGET_ADDR', '')

            except Exception as e:
                msg = str(e) or type(e).__name__
                cls.status = f'broken .env file ({fn}: {msg})'
                return
            fn = os.path.join(
                cls.compose_path,
                'data',
                'config',
                'infrasonar.yaml')
            try:
                with open(fn, 'r') as fp:
                    cls.config_data = yaml.safe_load(fp)
                    assert isinstance(cls.config_data, dict)
            except Exception:
                cls.config_data = {}  # file is not required to exist

    @classmethod
    async def read_probes_config_meta(cls):
        url = f'{cls.api_url}/probes-config-meta.yml'
        async with ClientSession() as session:
            async with session.get(url, ssl=True) as r:
                r.raise_for_status()
                raw = await r.read()

        cls.probes_config_meta = yaml.safe_load(raw)

    @classmethod
    def get_probes(cls) -> List[str]:
        return sorted(
            key[:-6]
            for key in cls.compose_data['services'].keys()
            if key.endswith('-probe'))

    @classmethod
    def get_config_value(cls, keys: List[str], dval: Optional[Any] = None):
        d = cls.config_data
        for k in keys:
            if k is None:
                continue  # ignore None values in key
            if isinstance(d, dict):
                d = d.get(k)
        return dval if d is None else d

    @classmethod
    def get_env_var(cls, probe: str, key: str,
                    dval: Optional[Any] = None) -> str:
        services = State.compose_data['services']
        probedict = services.get(f'{probe}-probe', {})
        environment = probedict.get('environment', {})
        return environment.get(key, dval)


class Pos(NamedTuple):
    y: int
    x: int


class MenuItem(NamedTuple):
    name: str
    func: callable


class Menu:
    def __init__(self, win, pos: Pos, items: Tuple[Optional[MenuItem]],
                 horizontal: bool = False, ljust: Optional[int] = None,
                 idx: Optional[int] = None):
        assert isinstance(items[0], MenuItem), 'first must be a MenuItem'
        assert isinstance(items[-1], MenuItem), 'last must be a MenuItem'
        self.win = win
        self.pos = pos
        self.idx = max(min(idx or 0, len(items)), 0)
        self.items = items
        self.horizontal = horizontal
        self.pad = ljust
        self.draw()

    def draw(self):
        maxy, _maxx = self.win.getmaxyx()

        # not perfect for horizontal but we can ignore this
        m = maxy-self.pos.y-1
        s = max(self.idx-m+1, 0)
        items = self.items[s:s+m]

        for idx, item in enumerate(items):
            if item is None:
                if self.horizontal is False and self.pad is not None:
                    self.win.addstr(self.pos.y+idx, self.pos.x, ' '*self.pad)
                continue
            mode = curses.A_REVERSE if idx+s == self.idx else curses.A_NORMAL
            if self.horizontal:
                y = self.pos.y
                x = self.pos.x + sum([
                    len(item.name) + 1
                    for item in self.items[:idx]
                    if item is not None])
            else:
                y, x = self.pos.y+idx, self.pos.x
            k = item.name if self.pad is None else item.name.ljust(self.pad)

            self.win.addstr(y, x, k, mode)
        self.win.refresh()

    def handle_char(self, char: int):
        if char == 27:
            self.items[-1].func()
        if char == curses.KEY_UP or char == curses.KEY_LEFT:
            self.idx -= 1
            if self.idx < 0:
                self.idx = len(self.items)-1
        elif char == curses.KEY_DOWN or char == curses.KEY_RIGHT or char == 9:
            self.idx += 1
            if self.idx == len(self.items):
                self.idx = 0
        elif char == curses.KEY_ENTER or char == 10 or char == 13:
            self.items[self.idx].func()
            return

        if self.items[self.idx] is None:
            self.handle_char(char)
        else:
            self.draw()


class Input:
    def __init__(self, stdscr, title: str, confirm: callable,
                 cancel: callable):
        self.stdscr = stdscr
        self.title = title
        self.confirm = confirm
        self.cancel = cancel

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def handle_char(self, char: int):
        pass


class InputStr(Input):
    def __init__(self, stdscr, title: str, confirm: callable, cancel: callable,
                 validate: callable, text: str, charset: set,
                 max_len: int = 60, secret: bool = False):
        super().__init__(stdscr, title, confirm, cancel)
        if not isinstance(text, str):
            text = str(text)

        self.secret = secret
        self.hide = secret
        self.text = text
        self.curs_x = len(self.text)
        self.validate = validate
        self.charset = charset
        self.max_len = max_len

    async def _set_cursor(self):
        curses.setsyx(self.wpos.y + 4, self.wpos.x + 2 + self.curs_x)
        curses.doupdate()

    def draw(self):
        maxy, maxx = self.stdscr.getmaxyx()
        h, w = 9, 65

        curses.curs_set(2)

        self.wpos = Pos(maxy//2-h//2, maxx//2-w//2)
        self.win = self.stdscr.subwin(h, w, self.wpos.y, self.wpos.x)
        self.win.bkgd(' ', curses.color_pair(3) | curses.A_BOLD)
        self.win.erase()
        self.win.box()
        self.win.addstr(2, 2, self.title)

        enter = ', ENTER to confirm' if self.validate(self.text) else ''
        secret = 'CTRL+h to show/hide, ' if self.secret else ''
        msg = f'({secret}ESC to cancel{enter})'
        self.win.addstr(7, 63 - len(msg), msg)

        textstr = '*' * len(self.text) if self.hide else self.text
        textstr = textstr.ljust(min(self.max_len+10, 61))
        self.win.addstr(4, 2, textstr, curses.A_REVERSE)
        self.win.refresh()

        asyncio.ensure_future(self._set_cursor())

    def handle_char(self, char: int):
        if char == curses.KEY_LEFT:
            if self.curs_x:
                self.curs_x -= 1
        elif char == curses.KEY_RIGHT:
            if self.curs_x < len(self.text):
                self.curs_x += 1
        elif char == curses.KEY_HOME:
            self.curs_x = 0
        elif char == curses.KEY_END:
            self.curs_x = len(self.text)
        elif char == 263 and self.secret:  # CTRL+h
            self.hide = not self.hide
        elif char == curses.KEY_BACKSPACE or char == 127:
            if self.curs_x:
                self.text = \
                    self.text[:self.curs_x-1] + self.text[self.curs_x:]
                self.curs_x -= 1
        elif char == 330:  # DELETE
            self.text = self.text[:self.curs_x] + self.text[self.curs_x+1:]
        elif char == curses.KEY_ENTER or char == 10 or char == 13:
            if self.validate(self.text):
                self.confirm(self.text)
                return
        elif char == 27:  # ESCAPE
            self.cancel()
            return
        elif char in self.charset:
            if len(self.text) < self.max_len:
                self.text = (
                    self.text[:self.curs_x] +
                    chr(char) +
                    self.text[self.curs_x:])
                self.curs_x += 1
        self.draw()


class InputInt(Input):

    def __init__(self, stdscr, title: str, confirm: callable, cancel: callable,
                 number: int, mi: int, ma: int):
        super().__init__(stdscr, title, confirm, cancel)
        if not isinstance(number, int):
            try:
                number = int(number)
            except Exception:
                number = 0

        self.number = number
        self.mi = mi
        self.ma = ma

    def draw(self):
        maxy, maxx = self.stdscr.getmaxyx()
        h, w = 9, 65

        self.wpos = Pos(maxy//2-h//2, maxx//2-w//2)
        self.win = self.stdscr.subwin(h, w, self.wpos.y, self.wpos.x)
        self.win.bkgd(' ', curses.color_pair(3) | curses.A_BOLD)
        self.win.erase()
        self.win.box()
        self.win.addstr(2, 2, self.title)

        msg = \
            '(Up/Down+-1, PgUp/Down+-10, ' \
            'ENTER to confirm, ESC to Cancel)'

        self.win.addstr(7, 63 - len(msg), msg)

        numberstr = str(self.number).rjust(6)
        self.win.addstr(4, 2, numberstr, curses.A_REVERSE)
        self.win.refresh()

    def handle_char(self, char: int):
        if char == curses.KEY_UP:
            if self.number < self.ma:
                self.number += 1
        elif char == curses.KEY_DOWN:
            if self.number > self.mi:
                self.number -= 1
        elif char == 339:  # PgUp
            self.number += 10
            self.number = min(self.ma, self.number)
        elif char == 338:  # PgDown
            self.number -= 10
            self.number = max(self.mi, self.number)
        elif char == curses.KEY_ENTER or char == 10 or char == 13:
            self.confirm(self.number)
            return
        elif char == 27:  # ESCAPE
            self.cancel()
            return
        self.draw()


class InputList(Input):

    def __init__(self, stdscr, title: str, confirm: callable, cancel: callable,
                 options: List[Any], selected: Any):
        super().__init__(stdscr, title, confirm, cancel)
        self.options = options
        self.selected = selected
        self.menu: Optional[Menu] = None

    def on_select(self, option):
        self.selected = option
        self.menu.idx = len(self.options) + 1
        self.draw()

    def draw(self):
        maxy, maxx = self.stdscr.getmaxyx()
        h, w = len(self.options)+8, 65

        self.wpos = Pos(maxy//2-h//2, maxx//2-w//2)
        self.win = self.stdscr.subwin(h, w, self.wpos.y, self.wpos.x)
        self.win.bkgd(' ', curses.color_pair(3) | curses.A_BOLD)
        self.win.erase()
        self.win.box()
        self.win.addstr(2, 2, self.title)

        msg = '(ESC to cancel)'
        self.win.addstr(h-2, w-len(msg)-2, msg)

        items = []
        for option in self.options:
            items.append(MenuItem(
                f'* {option}' if option == self.selected else f'  {option}',
                functools.partial(self.on_select, option)
            ))

        items.append(None)
        items.append(MenuItem(
            '  Ok',
            functools.partial(self.confirm, self.selected)
        ))

        if self.menu:
            idx = self.menu.idx
        else:
            idx = 0
        self.menu = Menu(
            self.win,
            Pos(4, 4),
            items,
            ljust=25,
            idx=idx)
        self.win.refresh()

    def handle_char(self, char: int):
        if char == 27:  # ESCAPE
            self.cancel()
            return
        if char == 32:  # SPACE
            if self.menu.idx < len(self.menu.items)-1:
                char = 13  # ENTER
        if self.menu:
            self.menu.handle_char(char)
        self.draw()


def ensure_config_defaults(config: dict, source: List[dict]):
    for data in source:
        if 'int' in data:
            key = data['int']
            if key not in config:
                v = data.get('default', 0)
                config[key] = v
        elif 'str' in data:
            key = data['str']
            if key not in config:
                v = data.get('default', '')
                config[key] = v
        elif 'list' in data:
            key = data['list']
            if key not in config:
                v = data.get('default', data['options'][0])
                config[key] = v
        elif 'section' in data:
            key = data['section']
            if key not in config:
                config[key] = {}
            c = config[key]
            ensure_config_defaults(c, data['items'])


def _get_val_helper(probe: str, part: Part, section: Optional[str], key: str,
                    dval: Any):
    if part is Part.Config:
        keys = [probe, part.value, section, key]
        return State.get_config_value(keys, dval)

    return State.get_env_var(probe, key, dval)


class Confirm:
    def __init__(self, stdscr, msg: str, confirm: callable, cancel: callable):
        self.stdscr = stdscr
        self.msg = msg
        self.confirm = confirm
        self.cancel = cancel
        self.menu: Optional[Menu] = None

    def draw(self):
        maxy, maxx = self.stdscr.getmaxyx()
        width = min(maxx - 10, 120)
        lines = textwrap.wrap(self.msg, width=width-8)
        h, w = len(lines) + 6, width
        self.win = self.stdscr.subwin(h, w, maxy//2-h//2, maxx//2-w//2)
        self.win.bkgd(' ', curses.color_pair(3) | curses.A_BOLD)
        self.win.erase()
        self.win.box()
        for n, s in enumerate(lines):
            self.win.addstr(n+2, 4, s)

        self.menu = Menu(self.win, Pos(4, 4), (
            MenuItem(' Yes ', self.confirm),
            MenuItem(' No ', self.cancel),
        ), horizontal=True, idx=1)


class Help:
    def __init__(self, stdscr, messages: List[str]):
        self.stdscr = stdscr
        self.messages = messages
        self.show = False

    def toggle(self):
        self.show = not self.show

    def draw(self):
        maxy, maxx = self.stdscr.getmaxyx()
        if not self.show:
            msg = "(press 'h' for help)"
            self.stdscr.addstr(maxy-2, maxx-len(msg)-2, msg)
            return
        width = min(maxx - 10, 120)
        lines = []
        for msg in self.messages:
            lines.extend(textwrap.wrap(msg, width=width-8))
            lines.append('')

        h, w = len(lines) + 5, width
        self.win = self.stdscr.subwin(h, w, maxy//2-h//2, maxx//2-w//2)
        self.win.bkgd(' ', curses.color_pair(3) | curses.A_BOLD)
        self.win.erase()
        self.win.box()
        for n, s in enumerate(lines):
            self.win.addstr(n+2, 4, s)
        msg = "(press 'q' to close)"
        self.win.addstr(h-2, w-len(msg)-2, msg)
        self.win.refresh()


class Fatal:
    def __init__(self, stdscr, msg: str, suggestion: Optional[str] = None):
        self.stdscr = stdscr
        self.msg = msg
        self.suggestion = suggestion
        self.draw()

    def draw(self):
        maxy, maxx = self.stdscr.getmaxyx()
        width = min(maxx - 10, 120)
        lines = textwrap.wrap(self.msg, width=width-8)
        if self.suggestion:
            lines.append('')
            suggs = self.suggestion.splitlines()
            for sugg in suggs:
                if sugg == '':
                    lines.append('')
                else:
                    lines.extend(textwrap.wrap(sugg, width=width-8))
        lines.append('')
        lines.append("Press 'q' to quit")
        h, w = len(lines) + 4, width
        win = self.stdscr.subwin(h, w, maxy//2-h//2, maxx//2-w//2)
        win.bkgd(' ', curses.color_pair(2) | curses.A_BOLD)
        win.erase()
        win.box()
        for n, s in enumerate(lines):
            win.addstr(n+2, 4, s)
        win.refresh()


class LogView:
    def __init__(self, parent):
        self.process: asyncio.Process = None
        self.lines: List[str] = []
        self.parent = parent
        self.redraw: bool = False
        self.offset: Optional[int] = None
        self.viewport: Optional[Tuple[int, int]] = None
        self.future: Optional[asyncio.Future] = None

    async def start(self, probe: str, n: Optional[int] = None):
        self.stop()

        tail = f' -n {n}' if n is not None else ''
        cmd = f'docker logs infrasonar-{probe}-probe-1 -f{tail}'
        self.process = await asyncio.create_subprocess_shell(
            cmd,
            stderr=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            cwd=State.compose_path)
        self.future = asyncio.ensure_future(self._read())
        await self.process.wait()

    async def _read(self):
        try:
            while True:
                line = await self.process.stderr.readline()
                if line:
                    line = line.decode()

                    # remove colors as this is not supported
                    line = _RE_COLOR.sub('', line)
                    self.lines.append(line)
                else:
                    break
        except Exception:
            pass

    def stop(self):
        if self.future:
            try:
                self.future.cancel()
            except Exception:
                pass
        if self.process:
            try:
                self.process.kill()

                # below is a fix for Python 3.12 (for some reason close is not
                # reached on the transport after calling kill or terminatre)
                self.process._transport.close()
            except Exception:
                pass
        self.future = None
        self.process = None
        self.lines.clear()

    def handle_char(self, char: int):
        if char == 27:  # ESC
            self.stop()
            self.parent.to_probe()
        elif char in (curses.KEY_UP, curses.KEY_DOWN, 338, 339,
                      curses.KEY_HOME, curses.KEY_END):
            if not self.viewport:
                return
            n, h = self.viewport
            m = n-h
            if self.offset is None:
                self.offset = m

            if char == curses.KEY_UP:
                self.offset -= 1
            elif char == curses.KEY_DOWN:
                self.offset += 1
            elif char == 339:  # PgUp
                self.offset -= h-1
            elif char == 338:  # PgDown
                self.offset += h-1
            elif char == curses.KEY_HOME:
                self.offset = 0
            elif char == curses.KEY_END:
                self.offset = m+1
            self.offset = max(0, self.offset)
            if self.offset > m:
                self.offset = None  # auto-scroll
            self.redraw = True


class InfraSonarDisplay:
    def __init__(self, stdscr: "_curses._CursesWindow"):
        self.stdscr = stdscr
        self.logview = LogView(self)
        self.confirm: Optional[Confirm] = None
        self.help: Optional[Help] = None
        self.input_dialog: Optional[Input] = None
        self.fatal: Optional[Fatal] = None
        self.main_menu: Optional[Menu] = None
        self.probes_menu: Optional[Menu] = None
        self.probe_menu: Optional[Menu] = None
        self.agents_menu: Optional[Menu] = None
        self.rapp_menu: Optional[Menu] = None
        self.probe: Optional[str] = None
        self.apply_step = 1
        self.skip_write = False
        self.done: bool = False
        self.warning: str = None
        self._spin: Optional(Pos) = None

    async def _spinner(self):
        spinner = '◐◓◑◒'  # '▁▂▃▄▅▆▇█▇▆▅▄▃'
        idx = 0
        while self._spin:
            self.stdscr.addstr(
                self._spin.y,
                self._spin.x,
                spinner[idx % len(spinner)])
            idx += 1
            await asyncio.sleep(0.1)

    def start_spinner(self, y: int, x: int):
        disabled = self._spin is None
        self._spin = Pos(y, x)
        if disabled:
            asyncio.ensure_future(self._spinner())

    def stop_spinner(self):
        self._spin = None

    def set_exit(self) -> None:
        self.logview.stop()
        self.done = True

    async def run(self) -> None:
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_CYAN)
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLUE)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
        self.stdscr.nodelay(True)
        self.stdscr.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
        self.make_display()

        while not self.done:
            char = self.stdscr.getch()
            if char == curses.ERR:
                await asyncio.sleep(0.1)
            elif char == curses.KEY_RESIZE:
                self.make_display()
            else:
                self.handle_char(char)

    def fatal_error(self, msg: str, suggestion: Optional[str] = None):
        self.confirm = None
        self.input_dialog = None
        self.fatal = Fatal(self.stdscr, msg, suggestion)

    async def check_root(self):
        y = 6
        self.stdscr.addstr(y, 4, "Check Root access........................")
        self.start_spinner(y, 45)
        try:
            assert os.geteuid() == 0, \
                'The InfraSonar appliance tool must run as root!!'
            await asyncio.sleep(0.1)
        except Exception as e:
            msg = str(e) or type(e).__name__
            self.fatal_error(msg, "Please start the tool again as root.")
        else:
            self.stdscr.addstr(y, 45, 'OK')
            await self.check_internet()
        finally:
            self.stop_spinner()

    async def check_internet(self):
        y = 7
        self.stdscr.addstr(y, 4, "Check Internet connection................")
        self.start_spinner(y, 45)
        try:
            async with ClientSession() as session:
                async with session.get(State.api_url, ssl=True) as r:
                    r.raise_for_status()
        except Exception as e:
            msg = str(e) or type(e).__name__
            msg = f"Failed to connect to: {State.api_url} (Error: {msg})"
            self.fatal_error(msg, "Please check your network configuration.")
        else:
            self.stdscr.addstr(y, 45, 'OK')
            await self.check_docker_installation()
        finally:
            self.stop_spinner()

    def confirm_probe_input(self, probe: str, part: Part,
                            section: Optional[str], key: str, value: Any):
        self.input_dialog = None
        if part is Part.Config:
            if State.config_data.get(probe) is None:
                State.config_data[probe] = {'config': {}}

            State.config_data[probe].pop('use', None)

            if State.config_data[probe].get('config') is None:
                State.config_data[probe]['config'] = {}
            if section:
                if State.config_data[probe]['config'].get(section) is None:
                    d = State.config_data[probe]['config'][section] = {}
                else:
                    d = State.config_data[probe]['config'][section]
            else:
                d = State.config_data[probe]['config']
        else:
            probe_key = f'{probe}-probe'
            if State.compose_data['services'].get(probe_key) is None:
                State.compose_data['services'][probe_key] = {}
            d = State.compose_data['services'][probe_key]
            if d.get('environment') is None:
                d['environment'] = {}
            else:
                # ensure a copy so it will not be shared
                d['environment'] = d['environment'].copy()
            d = d['environment']

        if value != d.get(key):
            State.has_changes = True  # config
            d[key] = value
        self.to_probe()

    def _gen_probe_input_str(self, title: str, probe, part, section, key,
                             data: dict) -> InputStr:
        if key in ('secret', 'password'):
            text = ''
            secret = True
        else:
            secret = False
            dval = data.get('default', '')
            text = _get_val_helper(probe, part, section, key, dval)
        regex = data.get('re')

        def validate(_: str) -> bool:
            return True

        if regex:
            try:
                rx = re.compile(regex)
            except Exception:
                pass
            else:
                def validate(s: str) -> bool:
                    return rx.match(s) is not None

        return InputStr(
            self.stdscr,
            title,
            functools.partial(
                self.confirm_probe_input,
                probe, part, section, key),
            self.to_probe,
            validate,
            text,
            PRINTABLE_CHARS,
            secret=secret)

    def _gen_probe_input_int(self, title: str, probe, part, section, key,
                             data: dict) -> InputInt:
        mi, ma = data.get('min', -99999), data.get('max', 99999)
        dval = data.get('default', 0)
        number = _get_val_helper(probe, part, section, key, dval)
        return InputInt(
            self.stdscr,
            title,
            functools.partial(
                self.confirm_probe_input,
                probe, part, section, key),
            self.to_probe,
            number,
            mi,
            ma)

    def _gen_probe_input_list(self, title: str, probe, part, section, key,
                              data: dict) -> InputList:
        options = data['options']
        dval = data.get('default', options[0])
        selected = _get_val_helper(probe, part, section, key, dval)
        return InputList(
            self.stdscr,
            title,
            functools.partial(
                self.confirm_probe_input,
                probe, part, section, key),
            self.to_probe,
            options,
            selected)

    def generate_input_items(self, source: List[dict], probe: str, part: Part,
                             section: Optional[str] = None) -> List[callable]:
        """The subject is either "environment" or "config".
        """
        items = []
        for data in source:
            if 'if' in data:
                assert part is Part.Config  # only supported by config
                ifdata = data['if']
                if '==' in ifdata:
                    key, target = ifdata.split('==')
                    compare = eq
                elif '!=' in ifdata:
                    key, target = ifdata.split('!=')
                    compare = ne
                target = target.strip()
                keys = [x.strip() for x in key.split('.')]
                keys.insert(0, probe)
                val = State.get_config_value(keys)
                if not compare(val, target):
                    continue  # skip when if- not true

            if 'section' in data:
                assert part is Part.Config  # only supported by config
                items.extend(self.generate_input_items(
                    data['items'],
                    probe,
                    part,
                    data['section']))
                continue

            s = f'.{section}' if section else ''
            if 'str' in data:
                key = data["str"]
                title = f'Set {part.value}{s}.{key}'
                items.append((title, functools.partial(
                    self._gen_probe_input_str,
                    title, probe, part, section, key, data)))
            elif 'int' in data:
                key = data['int']
                title = f'Set {part.value}{s}.{key}'
                items.append((title, functools.partial(
                    self._gen_probe_input_int,
                    title, probe, part, section, key, data)))
            elif 'list' in data:
                key = data['list']
                title = f'Set {part.value}{s}.{key}'
                items.append((title, functools.partial(
                    self._gen_probe_input_list,
                    title, probe, part, section, key, data)))

        return items

    async def check_docker_installation(self):
        y = 8
        self.stdscr.addstr(y, 4, "Check Docker installation................")
        self.start_spinner(y, 45)
        try:
            cmd = 'docker -v'
            proc = await asyncio.create_subprocess_shell(
                cmd,
                stderr=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
            )

            stdout, stderr = await proc.communicate()
            out = stdout.decode()
            err = stderr.decode()
            if 'not found' in err or 'not found' in out:
                raise DockerNotFound()
            if err:
                raise Exception(err)
            docker_version = read_docker_version(out)
            if not docker_version:
                raise DockerNoVersion()
            if docker_version[0] < _MIN_DOCKER_VERSION:
                raise DockerVersionTooOld(
                    '.'.join([str(i) for i in docker_version]))
        except DockerNotFound:
            self.fatal_error(
                'Docker is not found on your system.',
                f'Please install docker, see: {DockerNotFound.install_url}')
        except DockerNoVersion:
            self.fatal_error('Failed to read the docker version.')
        except DockerVersionTooOld as e:
            self.fatal_error(
                f'Docker version too old: {e}', 'Please upgrade docker.')
        except Exception as e:
            msg = str(e) or type(e).__name__
            self.fatal_error(f'Unexpected error: {msg}')
        else:
            self.stdscr.addstr(y, 45, 'OK')
            await self.check_probes_config_meta()
        finally:
            self.stop_spinner()

    async def check_probes_config_meta(self):
        y = 9
        self.stdscr.addstr(y, 4, "Check and update probes config meta......")
        self.start_spinner(y, 45)
        try:
            await State.read_probes_config_meta()
        except Exception as e:
            msg = str(e) or type(e).__name__
            msg = f"Failed to download probes config meta (Error: {msg})"
            self.fatal_error(msg, "Please check your network configuration.")
        else:
            self.stdscr.addstr(y, 45, 'OK')
            await self.check_infrasonar_installation()
        finally:
            self.stop_spinner()

    async def check_infrasonar_installation(self):
        y = 10
        self.stdscr.addstr(y, 4, "Check InfraSonar appliance status........")
        self.start_spinner(y, 45)
        try:
            cmd = 'docker compose ls'
            proc = await asyncio.create_subprocess_shell(
                cmd,
                stderr=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                cwd=State.compose_path,  # Compose path is None here
            )

            stdout, stderr = await proc.communicate()
            out = stdout.decode()
            err = stderr.decode()
            if err:
                raise Exception(err)
            State.read_infrasonar_status(out)
            if State.status == 'not found':
                raise InfraSonarNotFound()
            if State.status != 'running' and State.status != 'restarting':
                raise InfraSonarNotRunning()
            ac_env = State.compose_data['services']['agentcore']['environment']
            if ac_env.get('HUB_HOST', 'hub.infrasonar.com') != State.hub_host:
                raise InfraSonarWrongEnv()
            await State.read_running_probes()
        except InfraSonarNotFound:
            self.on_install()
            return
        except InfraSonarNotRunning:
            if State.status == 'not running':
                sugg = \
                    'Start the appliance using the following command:\n\n' \
                    '  docker compose ' \
                    f'-f {State.compose_path}/docker-compose.yml up -d'
            else:
                sugg = None
            self.fatal_error(f'InfraSonar status: {State.status}', sugg)
        except InfraSonarWrongEnv:
            self.fatal_error(
                'InfraSonar enviroment mismatch',
                'Please check the --development argument (see --help)')
        except Exception as e:
            msg = str(e) or type(e).__name__
            self.fatal_error(f'Unexpected error: {msg}')
        else:
            self.stdscr.addstr(y, 45, 'OK')
            await asyncio.sleep(0.2)
            self.to_main()

        finally:
            self.stop_spinner()

    def set_agentcore_token(self, token):
        if token != State.agentcore_token:
            State.agentcore_token = token
            State.has_changes = True
            self.main_menu = None
        self.to_main()

    def set_agent_token(self, token):
        if token != State.agent_token:
            State.agent_token = token
            State.has_changes = True
            self.main_menu = None
        self.to_main()

    def set_agentcore_zone_id(self, zone):
        if zone != State.agentcore_zone_id:
            State.agentcore_zone_id = zone
            State.has_changes = True
            self.main_menu = None
        self.to_main()

    def set_socat_target_addr(self, socat_target_addr: str):
        if socat_target_addr != State.socat_target_addr:
            State.socat_target_addr = socat_target_addr
            services = State.compose_data['services']
            if socat_target_addr:
                services['socat'] = _SOCAT
            else:
                try:
                    del services['socat']
                except KeyError:
                    pass
            State.has_changes = True
            self.main_menu = None
        self.to_main()

    def to_main(self):
        self.probe = None
        self.help: Optional[Help] = None
        self.warning: Optional[str] = None
        self.confirm: Optional[Confirm] = None
        self.input_dialog: Optional[Input] = None
        self.probes_menu: Optional[Menu] = None
        self.probe_menu: Optional[Menu] = None
        self.agents_menu: Optional[Menu] = None
        self.rapp_menu: Optional[Menu] = None
        self.apply_step = None
        curses.curs_set(0)
        State.step = Step.Main
        asyncio.ensure_future(self.async_make_display())

    def to_probes(self):
        self.help: Optional[Help] = None
        State.step = Step.ManageProbes
        asyncio.ensure_future(self.async_make_display())

    def to_probe(self):
        self.help: Optional[Help] = None
        self.input_dialog: Optional[Input] = None
        State.step = Step.ManageProbe
        curses.curs_set(0)
        asyncio.ensure_future(self.async_make_display())

    def to_agents(self):
        self.help: Optional[Help] = None
        self.confirm: Optional[Confirm] = None
        State.step = Step.ManageAgents
        curses.curs_set(0)
        asyncio.ensure_future(self.async_make_display())

    def to_rapp(self):
        self.help: Optional[Help] = None
        self.confirm: Optional[Confirm] = None
        State.step = Step.Rapp
        curses.curs_set(0)
        asyncio.ensure_future(self.async_make_display())

    async def async_make_display(self):
        self.make_display()

    def on_exit_without_saving(self):
        self.confirm = Confirm(
            self.stdscr,
            'Do you want to quit without saving?',
            self.set_exit,
            self.to_main)
        asyncio.ensure_future(self.async_make_display())

    def on_change_agentcore_token(self):
        self.input_dialog = InputStr(
            self.stdscr,
            'Agentcore token',
            self.set_agentcore_token,
            self.to_main,
            lambda x: len(x) == TOKEN_LEN,
            State.agentcore_token,
            charset=TOKEN_CHARS,
            max_len=TOKEN_LEN,
            secret=True)
        asyncio.ensure_future(self.async_make_display())

    def on_change_agent_token(self):
        self.input_dialog = InputStr(
            self.stdscr,
            'Agent token',
            self.set_agent_token,
            self.to_main,
            lambda x: len(x) == TOKEN_LEN,
            State.agent_token,
            charset=TOKEN_CHARS,
            max_len=TOKEN_LEN,
            secret=True)
        asyncio.ensure_future(self.async_make_display())

    def on_change_zone(self):
        self.input_dialog = InputInt(
            self.stdscr,
            'Zone',
            self.set_agentcore_zone_id,
            self.to_main,
            State.agentcore_zone_id,
            0,
            9)
        asyncio.ensure_future(self.async_make_display())

    def on_api_forwarder(self):
        self.input_dialog = InputStr(
            self.stdscr,
            'InfraSonar API target address (empty for disable)',
            self.set_socat_target_addr,
            self.to_main,
            lambda _: True,
            State.socat_target_addr,
            charset=SOCAT_TARGET_CHARS)
        asyncio.ensure_future(self.async_make_display())

    def on_install_done(self, zone_id: Optional[int] = None):
        if zone_id is not None:
            State.agentcore_zone_id = zone_id

        self.input_dialog = None

        watchtower = _X_INFRASONAR_TEMPLATE.copy()
        watchtower.update(_WATCH_TOWER)

        agentcore = _X_INFRASONAR_TEMPLATE.copy()
        agentcore.update(_AGENTCORE)

        docker_agent = _X_INFRASONAR_TEMPLATE.copy()
        docker_agent.update(_DOCKER_AGENT)

        State.compose_data = {
            'x-infrasonar-template': _X_INFRASONAR_TEMPLATE,
            'services': {
                'watchtower': watchtower,
                'agentcore': agentcore,
                'docker-agent': docker_agent,
            }
        }

        try:
            path = os.path.join(State.compose_path, 'data', 'config')
            if not os.path.exists(path):
                os.makedirs(path)
        except Exception as e:
            msg = str(e) or type(e).__name__
            self.fatal_error(msg)
        else:
            self.save_and_apply_changes()

    def on_install_agentcore_zone_id(self, token: Optional[str] = None):
        if token is not None:
            State.agent_token = token

        self.input_dialog = InputInt(
            self.stdscr,
            'Enter your angetcore zone Id (leave 0 if unsure)',
            self.on_install_done,
            self.on_install_agent_token,
            State.agentcore_zone_id or 0,
            0,
            9)
        asyncio.ensure_future(self.async_make_display())

    def on_install_agent_token(self, token: Optional[str] = None):
        if token is not None:
            State.agentcore_token = token

        self.input_dialog = InputStr(
            self.stdscr,
            'Enter your agent token',
            self.on_install_agentcore_zone_id,
            self.on_install_agentcore_token,
            lambda x: len(x) == TOKEN_LEN,
            State.agent_token or '',
            charset=TOKEN_CHARS,
            max_len=TOKEN_LEN,
            secret=True)
        asyncio.ensure_future(self.async_make_display())

    def on_install_agentcore_token(self, path: Optional[str] = None):
        if path is not None:
            State.compose_path = os.path.abspath(path)

        self.input_dialog = InputStr(
            self.stdscr,
            'Enter your agentcore token',
            self.on_install_agent_token,
            self.on_install,
            lambda x: len(x) == TOKEN_LEN,
            State.agentcore_token or '',
            charset=TOKEN_CHARS,
            max_len=TOKEN_LEN,
            secret=True)
        asyncio.ensure_future(self.async_make_display())

    def on_install(self):
        State.step = Step.Install

        if State.compose_path is None:
            State.compose_path = '/etc/infrasonar'

        self.input_dialog = InputStr(
            self.stdscr,
            'Where do you want to install InfraSonar?',
            self.on_install_agentcore_token,
            self.set_exit,
            lambda _: True,
            State.compose_path,
            PRINTABLE_CHARS,
            max_len=60,
            secret=False)
        asyncio.ensure_future(self.async_make_display())

    def on_manage_probes(self):
        self.help: Optional[Help] = None
        State.step = Step.ManageProbes
        asyncio.ensure_future(self.async_make_display())

    def on_manage_agents(self):
        self.help: Optional[Help] = None
        State.step = Step.ManageAgents
        asyncio.ensure_future(self.async_make_display())

    def on_rapp(self):
        self.help: Optional[Help] = None
        State.step = Step.Rapp
        asyncio.ensure_future(self.async_make_display())

    def on_view_logs(self):
        self.help: Optional[Help] = None
        self.logview.viewport = None
        self.logview.offset = None
        asyncio.ensure_future(self.logview.start(self.probe))
        State.step = Step.ViewLogs
        asyncio.ensure_future(self.on_view_logs_display())

    async def write_to_disk(self):
        try:
            State.write()
        except Exception as e:
            return self.fatal_error(str(e))
        await asyncio.sleep(0.3)
        self.apply_step += 1
        self.draw_apply()
        await self.docker_compose_pull()

    async def docker_compose_pull(self):
        try:
            cmd = 'docker compose pull'
            proc = await asyncio.create_subprocess_shell(
                cmd,
                stderr=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                cwd=State.compose_path,
            )

            stdout, stderr = await proc.communicate()
            _out = stdout.decode()
            _err = stderr.decode()
        except Exception as e:
            return self.fatal_error(str(e))
        self.apply_step += 1
        self.draw_apply()
        await self.docker_compose_up()

    async def docker_compose_up(self):
        try:
            cmd = 'docker compose up -d --remove-orphans'
            proc = await asyncio.create_subprocess_shell(
                cmd,
                stderr=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                cwd=State.compose_path,
            )

            stdout, stderr = await proc.communicate()
            _out = stdout.decode()
            _err = stderr.decode()
        except Exception as e:
            return self.fatal_error(str(e))
        self.apply_step += 1
        self.draw_apply()
        await self.read_running_probes()

    async def read_running_probes(self):
        await State.read_running_probes()
        self.apply_step += 1
        self.draw_apply()

    def save_and_apply_changes(self):
        self.apply_step = 1
        self.skip_write = False
        State.step = Step.Apply
        self.main_menu: Optional[Menu] = None
        asyncio.ensure_future(self.async_make_display())
        asyncio.ensure_future(self.write_to_disk())

    def on_update(self):
        self.apply_step = 2
        self.skip_write = True
        State.step = Step.Apply
        self.main_menu: Optional[Menu] = None
        asyncio.ensure_future(self.async_make_display())
        asyncio.ensure_future(self.docker_compose_pull())

    def draw_apply(self):
        self.add_header()
        y, x = 7, 33
        self.stdscr.addstr(
            y, 4, "(Each step might take several minutes, please be patient!)")

        y += 1
        if not self.skip_write:
            y += 1
            self.stdscr.addstr(y, 4, "write changes to disk........")
        if self.apply_step > 1:
            if not self.skip_write:
                self.stdscr.addstr(y, x, "OK")
            y += 1
            self.stdscr.addstr(y, 4, "docker compose pull..........")
        if self.apply_step > 2:
            self.stdscr.addstr(y, x, "OK")
            y += 1
            self.stdscr.addstr(y, 4, "docker compose up............")
        if self.apply_step > 3:
            self.stdscr.addstr(y, x, "OK")
            y += 1
            self.stdscr.addstr(y, 4, "read running probes..........")

        if self.apply_step > 4:
            self.stdscr.addstr(y, x, "OK")
            y += 2
            self.stdscr.addstr(y, 4, "Done! (press any key to continue)")
            self.stop_spinner()
            State.has_changes = False
        else:
            self.start_spinner(y, x)

    def on_init(self):
        self.add_header()
        maxy, maxx = self.stdscr.getmaxyx()
        self.stdscr.addstr(maxy - 2, maxx - 20, "Press 'q' to quit")
        self.stdscr.refresh()

        # Ensure condif_data
        State.config_data = {}

        if self.fatal:
            self.fatal.draw()
        else:
            for signame in ('SIGINT', 'SIGTERM'):
                State.loop.add_signal_handler(
                    getattr(signal, signame), self.set_exit)

            asyncio.ensure_future(self.check_root())

    def on_use_confirm(self, selected: str):
        selected = None if selected == 'none' else selected
        if State.config_data.get(self.probe) is None:
            State.config_data[self.probe] = {}
        probe_cnf = State.config_data[self.probe]
        current = probe_cnf.get('use')
        if current != selected:
            State.has_changes = True
            if selected is None:
                probe_cnf.pop('use', None)
                config = probe_cnf['config'] = {}
                meta = State.probes_config_meta.get(self.probe, {})
                meta_cnf = meta.get('config')
                if meta_cnf:
                    ensure_config_defaults(config, meta_cnf)
            else:
                probe_cnf.pop('config', None)
                probe_cnf['use'] = selected
        self.to_probe()

    def on_use(self, use_options: set, use: Optional[str]):
        options = ['none'] + sorted(use_options)
        self.input_dialog = InputList(
            self.stdscr,
            'Select which configuration to use',
            self.on_use_confirm,
            self.to_probe,
            options,
            selected='none' if use is None else use)
        asyncio.ensure_future(self.async_make_display())

    def on_main(self):
        self.add_header()
        maxy, maxx = self.stdscr.getmaxyx()
        msg = f"InfraSonar status: {State.status}"
        self.stdscr.addstr(maxy - 2, maxx - len(msg) - 2, msg)
        self.stdscr.refresh()

        idx = self.main_menu.idx if self.main_menu else 0
        items = [
            MenuItem(
                'Manage probes',
                self.on_manage_probes),
            MenuItem(
                'Manage agents',
                self.on_manage_agents),
            None,
            MenuItem(
                'Change agentcore token',
                self.on_change_agentcore_token),
            MenuItem(
                'Change agent token',
                self.on_change_agent_token),
            MenuItem(
                'Change zone',
                self.on_change_zone),
            MenuItem(
                'Configure API forwarder',
                self.on_api_forwarder),
            MenuItem(
                'Remote appliance',
                self.on_rapp),
            None,
        ]

        if State.has_changes:
            items.extend([
                MenuItem(
                    'Save and apply changes',
                    self.save_and_apply_changes),
                MenuItem(
                    'Exit without saving',
                    self.on_exit_without_saving),
            ])
        else:
            items.extend([
                MenuItem(
                    'Pull and update',
                    self.on_update),
                MenuItem('Exit', self.set_exit),
            ])

        self.main_menu = Menu(
            self.stdscr, Pos(6, 4), items, horizontal=False, ljust=30, idx=idx)

        if self.confirm:
            self.confirm.draw()

        if self.input_dialog:
            self.input_dialog.draw()

    async def _on_synchronize_probes(self, y: int):
        State.step = Step.Synchronize
        self.warning: Optional[str] = None
        self.start_spinner(y, 2)
        try:
            await State.refresh_enbled_probes()
            await asyncio.sleep(1)
        except Exception as e:
            self.warning = str(e) or type(e).__name__
        self.stop_spinner()
        State.step = Step.ManageProbes
        self.probes_menu: Optional[Menu] = None
        self.make_display()

    def on_synchronize_probes(self, y: int):
        asyncio.ensure_future(self._on_synchronize_probes(y))

    def on_manage_probe(self, probe):
        State.step = Step.ManageProbe
        self.help: Optional[Help] = None
        self.probe_menu: Optional[Menu] = None
        self.probe = probe
        asyncio.ensure_future(self.async_make_display())

    def on_probe_set(self, input_dialog: Input):
        self.input_dialog = input_dialog()
        asyncio.ensure_future(self.async_make_display())

    def do_install_agent(self, agent: str):
        State.has_changes = True
        d = State.compose_data['x-infrasonar-template'].copy()
        d.update(_AGENTS[agent])
        State.compose_data['services'][f'{agent}-agent'] = d
        self.to_agents()

    def on_install_agent(self, agent: str):
        self.confirm = Confirm(
            self.stdscr,
            f'Are you sure you want to install the {agent} agent?',
            functools.partial(self.do_install_agent, agent),
            self.to_agents)
        asyncio.ensure_future(self.async_make_display())

    def do_remove_agent(self, agent: str):
        State.has_changes = True
        State.compose_data['services'].pop(f'{agent}-agent', None)
        self.to_agents()

    def on_remove_agent(self, agent: str):
        self.confirm = Confirm(
            self.stdscr,
            f'Are you sure you want to remove the {agent} agent?',
            functools.partial(self.do_remove_agent, agent),
            self.to_agents)
        asyncio.ensure_future(self.async_make_display())

    def do_install_rapp(self):
        State.has_changes = True
        d = State.compose_data['x-infrasonar-template'].copy()
        d.update(get_rapp(State.compose_path, USE_DEVELOPMENT))
        State.compose_data['services']['rapp'] = d
        self.to_rapp()

    def on_install_rapp(self):
        self.confirm = Confirm(
            self.stdscr,
            'Are you sure you want to install the remote appliance (RAPP)?',
            self.do_install_rapp,
            self.to_rapp)
        asyncio.ensure_future(self.async_make_display())

    def do_remove_rapp(self):
        State.has_changes = True
        State.compose_data['services'].pop('rapp', None)
        self.to_rapp()

    def on_remove_rapp(self):
        self.confirm = Confirm(
            self.stdscr,
            'Are you sure you want to remove the remote appliance (RAPP)?',
            self.do_remove_rapp,
            self.to_rapp)
        asyncio.ensure_future(self.async_make_display())

    async def on_view_logs_display(self):
        numlines = -1
        while State.step is Step.ViewLogs:
            if numlines == len(self.logview.lines) and \
                    self.logview.redraw is False:
                await asyncio.sleep(0.1)
                continue
            numlines = len(self.logview.lines)
            self.logview.redraw = False

            maxy, maxx = self.stdscr.getmaxyx()
            self.stdscr.erase()
            if maxx < 80 or maxy < 20:
                continue

            self.stdscr.box()

            h = maxy-3
            w = maxx-2
            win = self.stdscr.subwin(h, w, 1, 1)
            win.bkgd(' ', curses.color_pair(5))
            win.erase()

            lines = []
            for line in self.logview.lines:
                lines.extend(textwrap.wrap(line, width=w))

            # update view port
            self.logview.viewport = (len(lines), h)

            if self.logview.offset is None:
                lines = lines[-h:]
                autoscroll = ', autoscroll'
            else:
                offset = self.logview.offset
                lines = lines[offset:offset+h]
                autoscroll = ''

            for y, line in enumerate(lines):
                win.addstr(y, 0, line)

            msg = \
                f'({self.probe}{autoscroll}, Arrow/PgUp/Down, ESC=exit)'
            self.stdscr.addstr(maxy-2, maxx-len(msg)-2, msg)

    def on_manage_agents_display(self):
        self.add_header()
        items = []
        for agent in _AGENTS:

            if State.compose_data['services'].get(f'{agent}-agent') is None:
                items.append(MenuItem(
                    f'Install {agent} agent',
                    functools.partial(self.on_install_agent, agent)
                ))
            else:
                items.append(MenuItem(
                    f'Remove {agent} agent',
                    functools.partial(self.on_remove_agent, agent)
                ))

        items.append(None)
        items.append(MenuItem(
            'Back to main',
            self.to_main
        ))

        idx = self.agents_menu.idx if self.agents_menu else 0
        self.agents_menu = Menu(
            self.stdscr,
            Pos(6, 4),
            items,
            horizontal=False,
            ljust=30,
            idx=idx)

        if self.confirm:
            self.confirm.draw()

    def on_rapp_display(self):
        self.add_header()
        items = []
        if State.compose_data['services'].get('rapp') is None:
            items.append(MenuItem(
                'Install Remote Appliance (RAPP)',
                self.on_install_rapp
            ))
        else:
            items.append(MenuItem(
                'Remove Remote Appliance (RAPP)',
                self.on_remove_rapp
            ))

        items.append(None)
        items.append(MenuItem(
            'Back to main',
            self.to_main
        ))

        idx = self.rapp_menu.idx if self.rapp_menu else 0
        self.rapp_menu = Menu(
            self.stdscr,
            Pos(6, 4),
            items,
            horizontal=False,
            ljust=30,
            idx=idx)

        if self.confirm:
            self.confirm.draw()

    def on_select_branch(self, branch: str):
        current = State.get_probe_tag(self.probe)
        if current != branch:
            State.has_changes = True
            if branch == 'stable':
                tag = ''
            else:
                tag = f':{branch}'

            p = State.compose_data['services'][f'{self.probe}-probe']
            p['image'] = f'ghcr.io/infrasonar/{self.probe}-probe{tag}'
        self.to_probe()

    def on_choose_branch(self, branch: str):
        options = [
            'stable',
            'unstable'
        ]
        if branch not in options:
            options.append(branch)
        self.input_dialog = InputList(
            self.stdscr,
            'Choose branch: (be careful with unstable)',
            self.on_select_branch,
            self.to_probe,
            options=options,
            selected=branch)
        asyncio.ensure_future(self.async_make_display())

    def on_manage_probe_display(self):
        maxy, maxx = self.stdscr.getmaxyx()
        meta = State.probes_config_meta
        meta_env = meta.get(self.probe, {}).get('environment', {})
        meta_cnf = meta.get(self.probe, {}).get('config', {})
        help = meta.get(self.probe, {}).get('help', '').splitlines()
        inputs: List[Input] = []
        items = []

        if meta_cnf:
            use_options = set()
            for k, v in meta.items():
                if k == self.probe:
                    continue
                if v.get('config') is meta_cnf and \
                        State.config_data.get(k, {}).get('config') is not None:
                    use_options.add(k)

            if self.probe not in State.config_data:
                State.has_changes = True
                config = {}
                ensure_config_defaults(config, meta_cnf)
                State.config_data[self.probe] = {'config': config}

            use = State.config_data.get(self.probe, {}).get('use')
            if not use:
                if State.config_data[self.probe].get('config') is None:
                    config = {}
                    ensure_config_defaults(config, meta_cnf)
                    State.config_data[self.probe]['config'] = config

                inputs.extend(self.generate_input_items(
                    meta_cnf,
                    self.probe,
                    Part.Config))
            else:
                use_options.add(use)

            if use_options:
                items.append(MenuItem(
                    f'Use: {use if use else "-"}',
                    functools.partial(
                        self.on_use,
                        use_options,
                        use)
                ))
                items.append(None)

        if meta_env:
            if inputs:
                inputs.append(None)
            inputs.extend(self.generate_input_items(
                meta_env,
                self.probe,
                Part.Environment))

        for inp in inputs:
            if inp is None:
                items.append(None)
            else:
                title, func = inp
                items.append(MenuItem(
                    title,
                    functools.partial(self.on_probe_set, func)
                ))

        if items:
            items.append(None)

        if State.has_changes:
            items.append(MenuItem(
                'Save and apply changes',
                self.save_and_apply_changes))

        branch = State.get_probe_tag(self.probe)
        items.append(MenuItem(
            f'Choose branch (current: {branch})',
            functools.partial(self.on_choose_branch, branch)
        ))

        idx = self.probe_menu.idx if self.probe_menu else len(items)

        if self.probe in State.running_probes:
            items.append(MenuItem(
                'View logs',
                self.on_view_logs,
            ))

        items.append(MenuItem(
            'Back',
            self.to_probes
        ))

        self.stdscr.addstr(2, 4, f'Collector: {self.probe}')
        self.stdscr.addstr(3, 4, '-'*50)

        self.probe_menu = Menu(
            self.stdscr,
            Pos(5, 4),
            items,
            ljust=50,
            idx=idx)

        if self.input_dialog:
            self.input_dialog.draw()

        if help:
            if not self.help:
                self.help = Help(self.stdscr, help)
            self.help.draw()

    def on_manage_probes_display(self):
        self.add_header()
        maxy, maxx = self.stdscr.getmaxyx()
        self.stdscr.refresh()

        messages = [
            "You can configure the probe collectors here.",
            "When you choose to synchronize, all enabled probes in your "
            "InfraSonar container will become available here, and disabled "
            "probes will be removed.",
            "A probe marked with (!) requires configuration that is "
            "currently missing.",
            "A probe marked with (~) is not on the stable branch."
        ]

        if self.help is None:
            self.help = Help(self.stdscr, messages)

        y = 6
        if self.warning:
            color = curses.color_pair(4)
            self.stdscr.addstr(y, 4, f':: {self.warning}', color)
            y += 2

        idx = self.probes_menu.idx if self.probes_menu else 0
        items = []
        for probe in State.get_probes():
            warn = ''
            required = State.probes_config_meta.get(probe, {}).get('config')
            probe_cnf = State.config_data.get(probe, {})
            conf_or_use = probe_cnf.get('config') or probe_cnf.get('use')
            if required and not conf_or_use:
                warn += '!'
            if State.get_probe_tag(probe) != 'stable':
                warn += '~'
            if warn:
                warn = f' ({warn})'
            items.append(MenuItem(
                f'{probe}{warn}',
                functools.partial(self.on_manage_probe, probe)
            ))
        if items:
            items.append(None)

        offset = len(items)
        items.append(MenuItem(
                'Synchronize',
                lambda: self.on_synchronize_probes(y+offset)))
        items.append(MenuItem(
            'Back to main',
            self.to_main))

        self.probes_menu = Menu(
            self.stdscr,
            Pos(y, 4),
            items,
            horizontal=False,
            ljust=30,
            idx=idx)

        self.help.draw()

    def add_header(self):
        msg = r"""    ___       __          ___
   |_ _|_ _  / _|_ _ __ _/ __| ___ _ _  __ _ _ _
    | || ' \|  _| '_/ _` \__ \/ _ \ ' \/ _` | '_|
   |___|_||_|_| |_| \__,_|___/\___/_||_\__,_|_|
"""

        for y, line in enumerate(msg.splitlines()):
            self.stdscr.addstr(1+y, 1, line)

    def make_display(self) -> None:
        maxy, maxx = self.stdscr.getmaxyx()
        self.stdscr.erase()
        if maxx < 80 or maxy < 20:
            return

        self.stdscr.box()

        if State.step is Step.Init:
            self.on_init()
        elif State.step is Step.Main:
            self.on_main()
        elif State.step is Step.Apply:
            self.draw_apply()
        elif State.step is Step.ManageProbes:
            self.on_manage_probes_display()
        elif State.step is Step.ManageProbe:
            self.on_manage_probe_display()
        elif State.step is Step.ManageAgents:
            self.on_manage_agents_display()
        elif State.step is Step.Rapp:
            self.on_rapp_display()
        elif State.step is Step.ViewLogs:
            self.logview.redraw = True
            self.logview.viewport = None
            self.logview.offset = None
        elif State.step is Step.Install:
            self.stdscr.refresh()
            self.input_dialog.draw()

    def handle_char(self, char: int) -> None:
        if self.input_dialog:
            self.input_dialog.handle_char(char)
        elif self.confirm:
            if self.confirm.menu:
                self.confirm.menu.handle_char(char)
        elif self.help and self.help.show:
            if char == 27 or chr(char) == 'q' or chr(char) == 'Q':
                self.help.toggle()
                self.make_display()
        elif self.help and (chr(char) == 'h' or chr(char) == 'H'):
            self.help.toggle()
            self.make_display()
        elif State.step is Step.Init or (
                State.step is Step.Apply and self.fatal):
            if chr(char) == 'q' or chr(char) == 'Q':
                self.set_exit()
        elif State.step is Step.Apply and self.apply_step > 3:
            if self.probe:
                self.to_probe()
            else:
                self.to_main()
        elif State.step is Step.ViewLogs:
            self.logview.handle_char(char)
        elif State.step is Step.Main:
            self.main_menu.handle_char(char)
        elif State.step is Step.ManageProbes:
            self.probes_menu.handle_char(char)
        elif State.step is Step.ManageProbe:
            self.probe_menu.handle_char(char)
        elif State.step is Step.ManageAgents:
            self.agents_menu.handle_char(char)
        elif State.step is Step.Rapp:
            self.rapp_menu.handle_char(char)


async def display_main(stdscr):
    disp = InfraSonarDisplay(stdscr)
    await disp.run()


def start(stdscr) -> None:
    # add signal handlers
    return State.loop.run_until_complete(display_main(stdscr))


def main():
    os.environ.setdefault('ESCDELAY', '25')
    setproctitle('appliance-manager')

    parser = argparse.ArgumentParser(prog='appliance-toolkit')
    parser.add_argument(
        '--version', '-v',
        action='store_true',
        help='Show version and exit')
    parser.add_argument(
        '--development',
        action='store_true',
        help='Use the InfraSonar development environment')

    args = parser.parse_args()

    if args.version:
        print(f'InfraSonar appliance toolkit version {__version__}')
        sys.exit(0)

    if args.development:
        global USE_DEVELOPMENT
        State.api_url = 'https://devapi.infrasonar.com'
        State.hub_host = 'devhub.infrasonar.com'
        USE_DEVELOPMENT = 1
    else:
        State.api_url = 'https://api.infrasonar.com'
        State.hub_host = 'hub.infrasonar.com'

    _AGENTCORE['environment']['HUB_HOST'] = State.hub_host
    _SPEEDTEST_AGENT['environment']['API_URI'] = State.api_url
    _DOCKER_AGENT['environment']['API_URI'] = State.api_url

    curses.wrapper(start)


if __name__ == '__main__':
    main()
