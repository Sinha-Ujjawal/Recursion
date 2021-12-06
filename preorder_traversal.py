from dataclasses import dataclass
from typing import Any, Iterable, Optional


@dataclass
class Node:
    value: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def preorder_traversal(node: Optional[Node]) -> Iterable[Any]:
    if node:
        yield node.value
        yield from preorder_traversal(node.left)
        yield from preorder_traversal(node.right)


def preorder_traversal_non_recursive(node: Optional[Node]) -> Iterable[Any]:
    CALL, HANDLE = 0, 1
    call_stack = [(CALL, node)]
    while call_stack:
        action, data = call_stack.pop()
        if action == CALL:
            node = data
            if node:
                call_stack.append((CALL, node.right))
                call_stack.append((CALL, node.left))
                call_stack.append((HANDLE, node))
        else:  # HANDLE
            node = data
            yield node.value


if __name__ == "__main__":
    tree = Node(
        1,
        Node(2, Node(4)),
        Node(3, Node(5)),
    )
    print(tree)
    print(list(preorder_traversal(tree)))
    print(list(preorder_traversal_non_recursive(tree)))
