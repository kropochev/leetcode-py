from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        """
        Consider all the leaves of a binary tree, from left to right order,
        the values of those leaves form a leaf value sequence.
        Two binary trees are considered leaf-similar if their leaf value
        sequence is the same.
        Return true if and only if the two given trees with head nodes root1
        and root2 are leaf-similar.

        >>> root1 = TreeNode(3)
        >>> root1.left = TreeNode(5)
        >>> root1.left.left = TreeNode(6)
        >>> root1.left.right = TreeNode(2)
        >>> root1.left.right.left = TreeNode(7)
        >>> root1.left.right.right = TreeNode(4)
        >>> root1.right = TreeNode(1)
        >>> root1.right.left = TreeNode(9)
        >>> root1.right.right = TreeNode(8)
        >>> root2 = TreeNode(3)
        >>> root2.left = TreeNode(5)
        >>> root2.left.left = TreeNode(6)
        >>> root2.left.right = TreeNode(7)
        >>> root2.right = TreeNode(1)
        >>> root2.right.left = TreeNode(4)
        >>> root2.right.right = TreeNode(2)
        >>> root2.right.right.left = TreeNode(9)
        >>> root2.right.right.right = TreeNode(8)
        >>> Solution().leafSimilar(root1, root2)
        True
        >>> root1 = TreeNode(1)
        >>> root1.left = TreeNode(2)
        >>> root1.right = TreeNode(3)
        >>> root2 = TreeNode(1)
        >>> root2.left = TreeNode(3)
        >>> root2.right = TreeNode(2)
        >>> Solution().leafSimilar(root1, root2)
        False
        """

        def getLeafs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            leaves = getLeafs(root.left) + getLeafs(root.right)
            return leaves

        return getLeafs(root1) == getLeafs(root2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
