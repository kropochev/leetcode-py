import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        You are given an array of k linked-lists lists, each linked-list
        is sorted in ascending order.

        Merge all the linked-lists into one sorted linked-list and return it.

        >>> list1 = ListNode(1, ListNode(4, ListNode(5)))
        >>> list2 = ListNode(1, ListNode(3, ListNode(4)))
        >>> list3 = ListNode(2, ListNode(6))
        >>> lists = [list1, list2, list3]
        >>> Solution().mergeKLists(lists)
        >>> lists = []
        >>> Solution().mergeKLists(lists)
        """
        h = []

        while lists:
            llist = lists.pop()
            if llist is not None:
                heapq.heappush(h, llist.val)
            if llist.next:
                lists.append(llist.next)

        def append(val):
            node = ListNode(val)
            if self.head is None:
                self.head = node
                return
            last = self.head
            while last.next:
                last = last.next
            last.next = node

        while h:
            append(heapq.heappop(h))

        return self.head


if __name__ == "__main__":
    import doctest

    doctest.testmod()
