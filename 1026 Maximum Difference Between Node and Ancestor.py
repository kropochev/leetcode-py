from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, find the maximum value v for which
        there exist different nodes a and b where v = |a.val - b.val| and
        a is an ancestor of b.

        A node a is an ancestor of b if either: any child of a is equal to b or
        any child of a is an ancestor of b.
        >>> root = TreeNode(8)
        >>> root.left = TreeNode(3)
        >>> root.left.left = TreeNode(1)
        >>> root.left.right = TreeNode(6)
        >>> root.left.right.left = TreeNode(4)
        >>> root.left.right.right = TreeNode(7)
        >>> root.right = TreeNode(10)
        >>> root.right.right = TreeNode(14)
        >>> root.right.right.left = TreeNode(13)
        >>> Solution().maxAncestorDiff(root)
        7
        >>> root = TreeNode(1)
        >>> root.right = TreeNode(2)
        >>> root.right.right = TreeNode(0)
        >>> root.right.right.left = TreeNode(3)
        >>> Solution().maxAncestorDiff(root)
        3
        """

        def dfs(node: Optional[TreeNode], low: int, hight: int) -> int:
            if not node:
                return hight - low
            low = min(low, node.val)
            hight = max(hight, node.val)
            return max(dfs(node.left, low, hight), dfs(node.right, low, hight))

        return dfs(root, root.val, root.val)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
