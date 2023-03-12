from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Given the root of a binary tree, check whether it is a mirror of itself
        (i.e., symmetric around its center).

        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(2)
        >>> root.left.left = TreeNode(3)
        >>> root.left.right = TreeNode(4)
        >>> root.right.left = TreeNode(4)
        >>> root.right.right = TreeNode(3)
        >>> Solution().isSymmetric(root)
        True
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(2)
        >>> root.left.right = TreeNode(3)
        >>> root.right.right = TreeNode(3)
        >>> Solution().isSymmetric(root)
        False
        """

        def isMirror(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if not root1 and not root2:
                return True
            if root1 and root2:
                if root1.val == root2.val:
                    return isMirror(root1.left, root2.right) and isMirror(
                        root1.right, root2.left
                    )
            return False

        return isMirror(root, root)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
