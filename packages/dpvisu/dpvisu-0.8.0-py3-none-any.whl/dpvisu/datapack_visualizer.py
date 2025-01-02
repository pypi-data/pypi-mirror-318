from diagrams import Diagram
from glob import iglob, glob
from pathlib import Path
import os
import sys
from .components import Advancement, Cluster, Function, FunctionTag, Node
from .components.call_manager import CallManager


def generate(
    data_dirs: list[Path],
    *,
    output_file: str = "datapack",
    format: str = "svg",
    show: bool = True,
) -> str:
    """Generate a diagram of the given datapacks. Returns path to file."""
    CallManager.start_new_diagram()
    datapacks: list[Path] = []
    for dir in data_dirs:
        datapacks.extend(_getDatapackPaths(dir))
    node_list: list[Node] = _makeNodeList(datapacks)
    print(f"Nodes: {len(node_list)}")
    return _generateGraph(
        node_list=node_list, output_file=output_file, format=format, show=show
    )


def _getDatapackPaths(raw_path: Path) -> list[Path]:
    if raw_path.name == "data":
        # Already in /data/ folder
        return [raw_path]
    else:
        # Assume root folder of datapack
        data_path = raw_path / "data"
        if data_path.exists():
            return [data_path]
        # Assume in /datapack/ directory. All relevant data directories should be 1 level deeper.
        return list(Path(raw_path).glob(r"*/data/"))


def _makeNodeList(datapacks: list[Path]) -> list[Node]:
    nodes = []
    for pack in datapacks:
        for path in pack.glob("**/*"):
            if path.is_dir():
                continue
            for kind in (Function, Advancement, FunctionTag):
                if kind.canDealWith(path.relative_to(pack)):
                    if artifact := kind.handleFile(file=path, base_pack=pack):
                        nodes.append(artifact)
                    break  # We are done with this file
    if not nodes:
        packs_string = "\n- ".join((pack.absolute().name for pack in datapacks))
        sys.exit(
            f"Error! There appear to be no files in the datapack. Are you sure these paths are correct?\n- {packs_string}"
        )
    return nodes


def _establishConnections(node_list: list[Node]):
    for node in node_list:
        node.createEdges()


def _generateGraph(*, output_file: str, node_list: list[Node], format: str, show: bool):
    with Diagram(
        name=output_file,
        graph_attr={
            "bgcolor": "#333333",
            "sep": "100",
            "fontcolor": "white",
            "rankdir": "TB",
            "splines": "ortho",
            "nodesep": "0.3",
            "ranksep": "1",
            "ordering": "in",
        },
        node_attr={
            "fontcolor": "white",
            "fontsize": "15.0",
            "shape": "box",
            "style": "solid",
            "labelloc": "c",
        },
        show=show,
        outformat=format,
    ) as d:
        Cluster.clusterize()
        _establishConnections(node_list)
        d.dot = d.dot.unflatten(stagger=3, fanout=True, chain=3)
        return f"{d.filename}.{format}"
