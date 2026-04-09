from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinearTimeSolution:
    def hasCycle(self, head: Optional[ListNode]):
        position_mappings, position = {}, 0
        if head is None:
            return None
        while head.next is not None:
            if head not in position_mappings:
                position_mappings[head] = position
                head = head.next
                position += 1
            else:
                return True
        else:
            return False
