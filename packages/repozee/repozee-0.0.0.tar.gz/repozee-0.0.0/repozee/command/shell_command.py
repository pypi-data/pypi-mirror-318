from pathlib import Path
from wizlib.parser import WizParser

from repozee.ai import AI
from repozee.command import RepoZeeCommand


class ShellCommand(RepoZeeCommand):

    name = 'shell'

    @classmethod
    def add_args(cls, parser: WizParser):
        super().add_args(parser)
        parser.add_argument('directory', default="", nargs='?')

    def handle_vals(self):
        super().handle_vals()
        if not self.provided('directory'):
            self.directory = str(Path.cwd())

    @RepoZeeCommand.wrap
    def execute(self):
        repozee = AI(self.directory)
        repozee.loop()
