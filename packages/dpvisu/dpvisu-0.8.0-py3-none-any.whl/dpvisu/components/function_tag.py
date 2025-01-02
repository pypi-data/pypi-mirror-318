import os
import re
from pathlib import Path
from typing import Self

from .abstract_node import AbstractNode
from .call_manager import CallManager
from .node import Node


class FunctionTag(AbstractNode):
    function_search_string = r'(?:")(\S+:\S+)(?:")'
    file_matcher: re.Pattern = re.compile(r'(?P<module>[^/]+)/tags?/functions?(?P<subpath>/.+)?/(?P<filename>[^/]+)\.json')

    def __init__(self, file: Path, data_folder: Path, *args, **kwargs):
        super().__init__(raw_file_path=file, data_folder_path=data_folder)

    @staticmethod
    def canDealWith(relative_file_path: Path) -> bool:
        return __class__.file_matcher.match(relative_file_path.as_posix()) is not None

    @staticmethod
    def handleFile(file: Path, base_pack: Path) -> None:
        if __class__.canDealWith(file.relative_to(base_pack)):
            FunctionTag(file, base_pack).generateCallList(file)
        return None

    def generateCallList(self, file: Path) -> Self:
        #search for function calls
        calls = AbstractNode._extractCallListFromFile(file, search_string=FunctionTag.function_search_string)
        for callee in calls:
            CallManager.registerCallToFunction(callee, self)
        return self

    @staticmethod
    def _generateCallName(relative_path: str) -> str:
        # Remove Extension
        path = os.path.normpath(relative_path)
        path = os.path.splitext(path)[0]

        # Remove 2nd & 3rd level of folder structure ("tags/function")
        path = path.replace(os.sep, '/')
        return "#" + re.sub('(/[A-z0-9_]+/[A-z0-9_]+/)', ':', path, count=1)
