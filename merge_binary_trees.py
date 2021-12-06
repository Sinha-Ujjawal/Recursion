from typing import Optional

# Leet Code - https://leetcode.com/problems/merge-two-binary-trees/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        CALL = 0
        HANDLE = 1
        call_stack = [(CALL, (root1, root2))]
        return_stack = []
        while call_stack:
            action, (n1, n2) = call_stack.pop()
            if action == CALL:
                if n1 == None:
                    return_stack.append(n2)
                elif n2 == None:
                    return_stack.append(n1)
                else:
                    call_stack.append((HANDLE, (n1, n2)))
                    call_stack.append((CALL, (n1.right, n2.right)))
                    call_stack.append((CALL, (n1.left, n2.left)))
            else:
                right_node = return_stack.pop()
                left_node = return_stack.pop()
                return_stack.append(
                    TreeNode(
                        val=n1.val + n2.val,
                        left=left_node,
                        right=right_node,
                    )
                )
        return return_stack[-1]
