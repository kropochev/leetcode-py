from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Given the root of a binary tree, invert the tree, and return its root.

        >>> root = TreeNode(4)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(7)
        >>> root.left.left = TreeNode(1)
        >>> root.left.right = TreeNode(3)
        >>> root.right.left = TreeNode(6)
        >>> root.right.right = TreeNode(9)
        >>> Solution().invertTree(root)
        """

        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


if __name__ == "__main__":
    import doctest

    doctest.testmod()
