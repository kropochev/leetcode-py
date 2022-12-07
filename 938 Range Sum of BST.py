from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Given the root node of a binary search tree and two integers low
        and high, return the sum of values of all nodes with a value
        in the inclusive range [low, high].

        >>> root = TreeNode(10)
        >>> root.left = TreeNode(5)
        >>> root.left.left = TreeNode(3)
        >>> root.left.right = TreeNode(7)
        >>> root.right = TreeNode(15)
        >>> root.right.right = TreeNode(18)
        >>> Solution().rangeSumBST(root, 7, 15)
        32
        >>> root = TreeNode(10)
        >>> root.left = TreeNode(5)
        >>> root.left.left = TreeNode(3)
        >>> root.left.left.left = TreeNode(1)
        >>> root.left.right = TreeNode(7)
        >>> root.left.right.left = TreeNode(6)
        >>> root.right = TreeNode(15)
        >>> root.right.left = TreeNode(13)
        >>> root.right.right = TreeNode(18)
        >>> Solution().rangeSumBST(root, 6, 10)
        23
        """

        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        return (
            root.val
            + self.rangeSumBST(root.right, low, high)
            + self.rangeSumBST(root.left, low, high)
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
