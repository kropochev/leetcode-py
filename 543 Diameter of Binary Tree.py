from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return the length of the diameter
        of the tree.

        The diameter of a binary tree is the length of the longest path between
        any two nodes in a tree. This path may or may not pass through the root.

        The length of a path between two nodes is represented by the number
        of edges between them.

        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(3)
        >>> root.left.left = TreeNode(4)
        >>> root.left.right = TreeNode(5)
        >>> Solution().diameterOfBinaryTree(root)
        3
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> Solution().diameterOfBinaryTree(root)
        1
        """
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def diameter(root):
            if root is None:
                return 0

            lheight = height(root.left)
            rheight = height(root.right)

            ldiameter = diameter(root.left)
            rdiameter = diameter(root.right)

            return max(lheight + rheight, max(ldiameter, rdiameter))

        return diameter(root)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
