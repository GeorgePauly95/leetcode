from typing import List, Optional


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class RecursiveSolution:
    def reverseList(
        self, head: Optional[ListNode], previous_node=None
    ) -> Optional[ListNode]:
        current_node = head
        if current_node is None:
            return None
        elif current_node.next is None:
            current_node.next = previous_node
            return current_node
        else:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            return self.reverseList(current_node, previous_node)


class IterativeSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node
