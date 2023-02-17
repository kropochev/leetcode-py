import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a Binary Search Tree (BST), return the minimum
        difference between the values of any two different nodes in the tree.
        >>> root = TreeNode(4)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(6)
        >>> root.left.left = TreeNode(1)
        >>> root.left.right = TreeNode(3)
        >>> Solution().getMinimumDifference(root)
        1
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(0)
        >>> root.right = TreeNode(48)
        >>> root.right.left = TreeNode(12)
        >>> root.right.right = TreeNode(49)
        >>> Solution().getMinimumDifference(root)
        1
        >>> root = TreeNode(90)
        >>> root.left = TreeNode(69)
        >>> root.left.left = TreeNode(49)
        >>> root.left.right = TreeNode(89)
        >>> root.left.left.right = TreeNode(52)
        >>> Solution().getMinimumDifference(root)
        1
        """
        current = root
        values, stack = [], []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                values.append(current.val)
                current = current.right
            else:
                break

        ans = math.inf
        for i in range(1, len(values)):
            ans = min(ans, values[i] - values[i-1])

        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
