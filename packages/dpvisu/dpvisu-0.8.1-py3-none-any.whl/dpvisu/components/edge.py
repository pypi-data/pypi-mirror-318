from colorsys import hsv_to_rgb
from random import random

from diagrams import Edge as OGEdge

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .node import Node

class Edge:
    @staticmethod
    def __makeEdge(tooltip=None) -> OGEdge:
        return OGEdge(color=Edge.__getRandomColor(), penwidth="3", tooltip=tooltip)

    @staticmethod
    def __getRandomColor() -> str:
        r, g, b = [hex(int(255 * i))[-2:] for i in hsv_to_rgb(random(), 0.5, 1.0)]
        return f'#{r}{g}{b}'

    @staticmethod
    def connect(node1: 'Node', node2: 'Node'):
        assert node1.obj is not None
        assert node2.obj is not None
        node1.obj >> Edge.__makeEdge(f'{node1.getMCName()} -> {node2.getMCName()}') >> node2.obj
