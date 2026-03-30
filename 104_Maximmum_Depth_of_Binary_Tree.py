from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_node, right_node = root.left, root.right
        if left_node is None and right_node is None:
            return 1
        return max(self.maxDepth(left_node), self.maxDepth(right_node)) + 1
