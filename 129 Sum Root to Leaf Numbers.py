from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        You are given the root of a binary tree containing digits from 0
        to 9 only.

        Each root-to-leaf path in the tree represents a number.

        For example, the root-to-leaf path 1 -> 2 -> 3 represents
        the number 123.
        Return the total sum of all root-to-leaf numbers. Test cases
        are generated so that the answer will fit in a 32-bit integer.

        A leaf node is a node with no children.

        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(3)
        >>> Solution().sumNumbers(root)
        25
        >>> root = TreeNode(4)
        >>> root.left = TreeNode(9)
        >>> root.right = TreeNode(0)
        >>> root.left.left = TreeNode(5)
        >>> root.left.right = TreeNode(1)
        >>> Solution().sumNumbers(root)
        1026
        """

        def pathSum(root, val=0):
            if not root:
                return 0

            val = val*10 + root.val
            if not root.left and not root.right:
                return val

            return pathSum(root.left, val) + pathSum(root.right, val)

        return pathSum(root)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
