from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        left_node = self.postorderTraversal(root.left)
        value = root.val
        right_node = self.postorderTraversal(root.right)
        return left_node + right_node + [value]
