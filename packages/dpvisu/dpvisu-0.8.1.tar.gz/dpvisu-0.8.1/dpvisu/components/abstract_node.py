import re
from abc import ABC, abstractmethod
from collections.abc import Generator
from pathlib import Path


class AbstractNode(ABC):
    """
        Abstract base class representing a file of a datapack.
        Cannot be drawn to a graph on its own, as not all files need graphical representation.
    """

    def __init__(self, raw_file_path: Path, data_folder_path: Path):
        self.relative_path: Path = raw_file_path.relative_to(data_folder_path)
        self._call_name = self._generateCallName(self.relative_path)

        self._display_name = self._generateDisplayName()
        self.generateCallList(raw_file_path)

    @staticmethod
    @abstractmethod
    def handleFile(file: Path, base_pack: Path):
        pass

    @abstractmethod
    def generateCallList(self, file: Path):
        pass

    @staticmethod
    @abstractmethod
    def canDealWith(relative_file_path: Path) -> bool:
        pass

    @staticmethod
    def _getRelativePath(file: Path, data_folder: Path) -> Path:
        return file.relative_to(data_folder)

    def getMCName(self):
        return self._call_name

    def __eq__(self, other: 'AbstractNode'):
        if not isinstance(other, AbstractNode):
            return NotImplemented
        return type(self) == type(other) and self.getMCName() == other.getMCName()

    def __hash__(self):
        return hash((self.getMCName(), type(self)))

    def _generateDisplayName(self) -> str:
        return self.getMCName().replace(':','/').split('/')[-1]

    @staticmethod
    def _generateCallName(relative_path: Path) -> str:
        # Remove Extension
        parts = relative_path.with_suffix('').parts
        # Replace "function" (or "advancement") with ":"
        module = parts[0]
        subpath = parts[2:]
        return f"{module}:{"/".join(subpath)}"

    @staticmethod
    def _iterLines(file: str) -> Generator[str]:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if not line.startswith("#") and len(line) > 1:
                    yield line

    @staticmethod
    def _extractCallListFromFile(file: Path, search_string: str) -> set[str]:
        calls = set()
        matcher = re.compile(search_string)
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if not line.startswith("#"):
                    match = matcher.search(line)
                    if match is not None:
                        calls.add(match.group(1))
        return set(calls)  # Eliminate duplicates
