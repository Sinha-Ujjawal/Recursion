from typing import Dict, Set, List, Tuple, Any, TypeVar
from collections import defaultdict

Node = TypeVar("Node")
Graph = Dict[Node, Set[Node]]


def depth_euler_traversal(g: Graph[Any], start: Any) -> Tuple[Dict[Any, Tuple[int, int]], List[int]]:
    CALL, HANDLE = 0, 1
    BEGIN, END = 0, 1
    stack = [(CALL, (start, 0))]
    traverse = []
    node_begin_end = defaultdict(lambda: [None, None])
    seen = {start}
    while stack:
        action, data = stack.pop(-1)
        if action == CALL:
            u, depth = data
            stack.append((HANDLE, (u, depth, END)))
            for v in g[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append((HANDLE, (u, depth, END)))
                    stack.append((CALL, (v, depth + 1)))
            stack.append((HANDLE, (u, depth, BEGIN)))
        else:
            u, depth, begin_or_end = data
            traverse.append(depth)
            if begin_or_end == BEGIN:
                if node_begin_end[u][0] is None:
                    node_begin_end[u][0] = len(traverse) - 1
            else: # END
                node_begin_end[u][1] = len(traverse) - 1
    return node_begin_end, traverse
