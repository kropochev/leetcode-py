from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Given the head of a singly linked list where elements are sorted
        in ascending order, convert it to a height-balanced binary search tree.
        >>> node = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
        >>> Solution().sortedListToBST(node)
        """
        vec = []
        temp = head
        while temp:
            vec.append(temp.val)
            temp = temp.next

        def sortedListToBSTRecur(vec, start, end):
            if start > end:
                return None
            mid = start + (end - start) // 2
            if (end - start) % 2 != 0:
                mid = mid + 1
            root = TreeNode(vec[mid])
            root.left = sortedListToBSTRecur(vec, start, mid - 1)
            root.right = sortedListToBSTRecur(vec, mid + 1, end)
            return root

        return sortedListToBSTRecur(vec, 0, len(vec) - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
