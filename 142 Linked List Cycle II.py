from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a linked list, return the node where the cycle
        begins. If there is no cycle, return null.
        There is a cycle in a linked list if there is some node in the list
        that can be reached again by continuously following the next pointer.
        Internally, pos is used to denote the index of the node that tail's
        next pointer is connected to (0-indexed). It is -1 if there is no cycle.
        Note that pos is not passed as a parameter.
        Do not modify the linked list.
        """
        if head is None or head.next is None:
            return 0
        fast = head
        slow = head
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return 0
