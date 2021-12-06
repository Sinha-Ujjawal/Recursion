from typing import Optional
from itertools import repeat

# Leet Code - https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        CALL, HANDLE = 0, 1
        call_stack = [(CALL, [root])]
        return_stack = []
        while call_stack:
            action, old_nodes = call_stack.pop()
            if old_nodes:
                if action == CALL:
                    childrens = []
                    for node in old_nodes:
                        if node:
                            childrens.append(node.left)
                            childrens.append(node.right)
                    call_stack.append((HANDLE, old_nodes))
                    call_stack.append((CALL, childrens))
                else:
                    childrens = (
                        iter(return_stack.pop()) if return_stack else repeat(None)
                    )
                    new_nodes = []
                    prev = None
                    for node in old_nodes:
                        if node:
                            nl = next(childrens)
                            nr = next(childrens)
                            new_node = Node(node.val, nl, nr)
                            new_nodes.append(new_node)
                            if prev:
                                prev.next = new_node
                            prev = new_node
                        else:
                            new_nodes.append(None)
                    return_stack.append(new_nodes)

        return return_stack[-1][0]
