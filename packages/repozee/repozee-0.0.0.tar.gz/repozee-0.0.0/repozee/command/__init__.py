from wizlib.command import WizCommand
from wizlib.parser import WizParser
from wizlib.ui import Choice, Chooser
from wizlib.command import CommandCancellation


class RepoZeeCommand(WizCommand):

    default = 'shell'
