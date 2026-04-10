class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        original_head = head
        if list1 is None and list2 is not None:
            return list2
        elif list1 is not None and list2 is None:
            return list1
        elif list1 is None and list2 is None:
            return None
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                head.val = list1.val
                list1 = list1.next
                if list1 is None:
                    break
                head.next = ListNode()
                head = head.next
            else:
                head.val = list2.val
                list2 = list2.next
                if list2 is None:
                    break
                head.next = ListNode()
                head = head.next
        if list1 is None and list2 is not None:
            head.next = list2
        elif list1 is not None and list2 is None:
            head.next = list1
