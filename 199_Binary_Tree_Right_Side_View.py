from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# use an array instead of a dictionary for result. Can use built-in insert method on array.
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


class RecursiveDFSSolution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        left_node, right_node = root.left, root.right
        right_result = self.rightSideView(right_node)
        left_result = self.rightSideView(left_node)
        right_length = len(right_result)
        return [root.val] + right_result + left_result[right_length:]
