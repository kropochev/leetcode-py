from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a singly linked list, group all the nodes with odd
        indices together followed by the nodes with even indices, and return
        the reordered list.

        The first node is considered odd, and the second node is even,
        and so on.

        Note that the relative order inside both the even and odd groups should
        remain as it was in the input.

        You must solve the problem in O(1) extra space complexity
        and O(n) time complexity.
        """

        if not head:
            return head

        evenStart = None
        evenEnd = None
        oddStart = None
        oddEnd = None
        currNode = head
        isEven = False

        while currNode:
            if isEven:
                isEven = False
                if not evenStart:
                    evenStart = currNode
                    evenEnd = evenStart
                else:
                    evenEnd.next = currNode
                    evenEnd = evenEnd.next
            else:
                isEven = True
                if not oddStart:
                    oddStart = currNode
                    oddEnd = oddStart
                else:
                    oddEnd.next = currNode
                    oddEnd = oddEnd.next

            currNode = currNode.next

        if not evenStart:
            return oddStart

        oddEnd.next = evenStart
        evenEnd.next = None

        return oddStart

