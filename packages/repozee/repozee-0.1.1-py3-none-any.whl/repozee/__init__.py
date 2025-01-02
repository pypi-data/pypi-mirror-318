from pathlib import Path
import inspect

from wizlib.app import WizApp
from wizlib.ui_handler import UIHandler
from wizlib.config_handler import ConfigHandler

from repozee.command import RepoZeeCommand


def load_definition(filename: str) -> str:
    """
    Load a definition file relative to the calling module's definitions
    directory.

    Args:
        filename: Name of file to load (e.g. 'system.md', 'tools.yml')

    Returns:
        String content of the file

    Raises:
        FileNotFoundError: If definitions directory or file doesn't exist
    """

    caller_frame = inspect.currentframe().f_back
    caller_file = Path(inspect.getframeinfo(caller_frame).filename)

    definitions_dir = caller_file.parent / 'definitions'
    if not definitions_dir.exists():
        raise FileNotFoundError(
            f"No definitions directory found at {definitions_dir}")

    file_path = definitions_dir / filename
    if not file_path.exists():
        raise FileNotFoundError(f"Definition file not found: {file_path}")

    return file_path.read_text()


class RepoZeeApp(WizApp):

    base = RepoZeeCommand
    name = 'repozee'
    handlers = [UIHandler, ConfigHandler]

    # def __init__(self, **handlers):
    #     super().__init__(**handlers)
    #     self.storage = FileStorage(self.config.get('busy-storage-directory'))

    # def run(self, **vals):
    #     super().run(**vals)
