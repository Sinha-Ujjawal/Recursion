from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    value: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def invert_binary_tree(node: Optional[Node]) -> Optional[Node]:
    if node == None:
        return None
    else:
        left_inverted = invert_binary_tree(node.left)
        right_inverted = invert_binary_tree(node.right)
        return Node(node.value, right_inverted, left_inverted)


def invert_binary_tree_non_recursive(node: Optional[Node]) -> Optional[Node]:
    CALL, HANDLE = 0, 1
    call_stack = [(CALL, node)]
    return_stack = []
    while call_stack:
        action, data = call_stack.pop()
        if action == CALL:
            node = data
            if node == None:
                return_stack.append(None)
            else:
                call_stack.append((HANDLE, node))
                call_stack.append((CALL, node.right))
                call_stack.append((CALL, node.left))
        else:  # HANDLE
            node = data
            right_inverted = return_stack.pop()
            left_inverted = return_stack.pop()
            return_stack.append(Node(node.value, right_inverted, left_inverted))

    return return_stack[-1] if return_stack else None


if __name__ == "__main__":
    tree = Node(
        1,
        Node(2, Node(4)),
        Node(3, Node(5)),
    )
    print(tree)
    print(invert_binary_tree(tree))
    print(invert_binary_tree_non_recursive(tree))
