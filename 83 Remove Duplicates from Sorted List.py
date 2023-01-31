from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Given the head of a sorted linked list, delete all duplicates such that
    each element appears only once. Return the linked list sorted as well.
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            ans = ListNode(head.val)
            tail = ans
        else:
            return None
        while head:
            if tail.val != head.val:
                tail.next = ListNode(head.val)
                tail = tail.next
            if head.next is None:
                break
            head = head.next
        return ans
