
from pathlib import Path
from gitignore_parser import parse_gitignore


class ProjectDir:

    def __init__(self, directory):
        self.directory = Path(directory)

    def list(self) -> list[str]:
        result = []
        gitignore = None
        gitignore_file = self.directory / '.gitignore'
        if gitignore_file.exists():
            gitignore = parse_gitignore(gitignore_file)
        for file_path in self.directory.rglob('*'):
            if '.git' in file_path.parts:
                continue
            if gitignore and gitignore(str(file_path)):
                continue
            result.append(str(file_path.relative_to(self.directory)))
        return result

    def read_file(self, file_path: str) -> str:
        path = self.directory / file_path
        return path.read_text()
