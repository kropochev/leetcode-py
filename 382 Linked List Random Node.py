from random import randint
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Given a singly linked list, return a random node's value from the linked
    list. Each node must have the same probability of being chosen.

    Implement the Solution class:
    Solution(ListNode head) Initializes the object with the head of
    the singly-linked list head.
    int getRandom() Chooses a node randomly from the list and returns its value.
    All the nodes of the list should be equally likely to be chosen.

    >>> head = ListNode(1, ListNode(2, ListNode(3)))
    >>> obj = Solution(head)
    >>> obj.getRandom()
    >>> obj.getRandom()
    >>> obj.getRandom()
    >>> obj.getRandom()
    >>> obj.getRandom()
    """

    def __init__(self, head: Optional[ListNode]):
        self.count = 0
        self.tail = head
        while self.tail.next:
            self.tail = self.tail.next
            self.count += 1
        self.tail.next = head

    def getRandom(self) -> int:
        cur = 0
        r = randint(0, self.count)
        while cur < r:
            self.tail = self.tail.next
            cur += 1

        return self.tail.val


if __name__ == "__main__":
    import doctest

    doctest.testmod()
