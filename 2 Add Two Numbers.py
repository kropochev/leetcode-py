from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        You are given two non-empty linked lists representing two non-negative
        integers. The digits are stored in reverse order,
        and each of their nodes contains a single digit.
        Add the two numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero,
        except the number 0 itself.
        """
        result = ListNode()
        tail = result
        s = 0
        while True:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            tail.val = (v1 + v2 + s) % 10
            s = (v1 + v2 + s) // 10
            if l1 is None and l2 is None:
                if s > 0:
                    tail.next = ListNode(s)
                break
            else:
                tail.next = ListNode()
                tail = tail.next

        return result
