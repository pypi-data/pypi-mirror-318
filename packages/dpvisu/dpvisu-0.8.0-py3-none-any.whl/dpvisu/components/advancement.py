import re
from pathlib import Path

from .call_manager import CallManager
from .edge import Edge
from .node import Node


class Advancement(Node):
    function_search_string = r'(?:"function"\s*:\s*")([^\s"]+)'
    file_matcher: re.Pattern = re.compile(r'(?P<module>[^/]+)/advancements?(?P<subpath>/.+)?/(?P<filename>[^/]+)\.json')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def canDealWith(relative_file_path: Path) -> bool:
        return __class__.file_matcher.match(relative_file_path.as_posix()) is not None

    @staticmethod
    def handleFile(file: Path, base_pack: Path) -> "Advancement":
        return Advancement(raw_file_path=file, data_folder_path=base_pack)

    def initObj(self):
        super()._initObj(colors = ["limegreen"])

    def generateCallList(self, file: Path):
        calls = Node._extractCallListFromFile(file, search_string=Advancement.function_search_string)
        for call in calls:
            CallManager.registerCallToFunction(call, self)

    def createEdges(self):
        cm = CallManager.getCallManagerOfAdvancement(self.getMCName())
        for caller in cm.registeredFunctions:
            Edge.connect(caller, self)
        self._is_root_node = not cm.hasCalls
