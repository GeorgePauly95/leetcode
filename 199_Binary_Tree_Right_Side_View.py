from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BFSSolution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue, result = [], {}
        if root is None:
            return []
        queue.append((root, 0))
        while len(queue) != 0:
            node, level = queue.pop(0)
            if node is not None:
                left_node, right_node = node.left, node.right
                queue.append((left_node, level + 1))
                queue.append((right_node, level + 1))
                result[level] = node.val
        return list(result.values())


class DFSSolution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [], {}
        if root is None:
            return []
        stack.append((root, 1))
        while len(stack) != 0:
            node, level = stack.pop(-1)
            if node is not None:
                left_node, right_node = node.left, node.right
                stack.append((right_node, level + 1))
                stack.append((left_node, level + 1))
                result[level] = node.val
        return list(result.values())
