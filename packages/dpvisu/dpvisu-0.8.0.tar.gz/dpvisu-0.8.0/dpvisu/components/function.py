import re
from pathlib import Path

from .call_manager import CallManager
from .edge import Edge
from .node import Node


class Function(Node):
    file_matcher: re.Pattern = re.compile(r'(?P<module>[^/]+)/functions?(?P<subpath>/.+)?/(?P<filename>[^/]+)\.mcfunction')
    function_matcher: re.Pattern = re.compile(r'(?:function )(\S+)')
    advancement_matcher: re.Pattern = re.compile(r'(?:advancement grant \S+ (?:only|until|through|from) )(\S+)(?:[$\s])?')

    def __init__(self, *args, **kwargs):
        self._is_macro: bool = False
        self._is_recursive: bool = False
        self.called_by_tags: list[str] = []

        super().__init__(*args, **kwargs)

    @staticmethod
    def canDealWith(relative_file_path: Path) -> bool:
        return __class__.file_matcher.match(relative_file_path.as_posix()) is not None

    @staticmethod
    def handleFile(file: Path, base_pack: Path) -> "Function":
            return Function(raw_file_path=file, data_folder_path=base_pack)

    def generateCallList(self, file: str):
        # search for function calls
        calls: list[str] = []
        own_name = self.getMCName()
        for line in Node._iterLines(file):
            if line.startswith("$"):
                self._is_macro = True

            if own_name.endswith("on_light_display_spawn"):
                pass
            function_match = Function.function_matcher.search(line)
            if function_match:
                callee = function_match.group(1)
                if callee == own_name:
                    self._is_recursive = True
                else:
                    calls.append(callee)
                    CallManager.registerCallToFunction(callee, self)
                continue

            advancement_match = Function.advancement_matcher.search(line)
            if advancement_match:
                CallManager.registerCallToAdvancement(advancement_match.group(1), self)
        print(f"{self._call_name} calls [" + ("\n".join(calls)) + "]")

    def initObj(self):
        colors = []
        # Single iteration or recursive
        colors.append("firebrick" if self._is_recursive else "royalblue4")

        cm = CallManager.getCallManagerOfFunction(self.getMCName())
        if not cm.hasCalls:
            self._is_root_node = True
            colors.append("darkorange2")
        else:
            for caller in cm.registeredFunctionTags:
                self.called_by_tags.append(caller.getMCName())
            if len(self.called_by_tags) > 0:
                # Called by a tag
                colors.append("purple")

        if self._is_macro:
            colors.append("magenta3")
        super()._initObj(colors)

    def createEdges(self):
        cm = CallManager.getCallManagerOfFunction(self.getMCName())
        for caller in cm.registeredNodes:
            Edge.connect(caller, self)

    def _getTooltip(self):
        return super()._getTooltip() + f"\nRecursive: {self._is_recursive}\nIs macro: {self._is_macro}\nCalled by Tags: [{', '.join(self.called_by_tags)}]"
