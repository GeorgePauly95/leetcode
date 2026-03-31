from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        print("root:", root)
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        value = root.val
        return [value] + left + right
