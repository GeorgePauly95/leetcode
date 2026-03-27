class Node:
    def __init__(self, value, right=None, left=None):
        self.right = right
        self.left = left
        self.value = value


def inorder(node):
    if node is None:
        return []
    left_value = inorder(node.left)
    root_value = [node.value]
    right_value = inorder(node.right)
    return left_value + root_value + right_value
