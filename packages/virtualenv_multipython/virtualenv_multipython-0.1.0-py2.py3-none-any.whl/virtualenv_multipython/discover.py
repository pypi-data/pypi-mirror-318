from pathlib import Path
import re

from virtualenv.discovery.builtin import Builtin
from virtualenv.discovery.discover import Discover
from virtualenv.discovery.py_info import PythonInfo


PATH_ROOT = Path('/usr/local/bin')

RX = (
    re.compile(r'(?P<impl>py)(?P<maj>[23])(?P<min>[0-9][0-9]?)'),
    re.compile(r'(?P<impl>py)(?P<maj>3)(?P<min>[0-9][0-9])(?P<suffix>t)'),
)


class Multipython(Discover):
    def __init__(self, options) -> None:
        super().__init__(options)
        self.builtin = Builtin(options)
        self.env = options.env['TOX_ENV_NAME']

    @classmethod
    def add_parser_arguments(cls, parser):
        Builtin.add_parser_arguments(parser)

    def run(self):
        for rx in RX:
            if match := rx.fullmatch(self.env):
                g = match.groupdict()
                name = {'py': 'python'}[g['impl']]
                command = f'{name}{g['maj']}.{g['min']}{g.get('suffix', '')}'
                return PythonInfo.from_exe(str(PATH_ROOT / command), resolve_to_host=False)
        return self.builtin.run()
