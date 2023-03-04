from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Given the root of a binary tree, return the postorder traversal of
        its nodes' values.

        >>> root = TreeNode(1)
        >>> root.right = TreeNode(2)
        >>> root.right.left = TreeNode(3)
        >>> Solution().postorderTraversal(root)
        [3, 2, 1]
        >>> Solution().postorderTraversal(None)
        []
        >>> root = TreeNode(1)
        >>> Solution().postorderTraversal(root)
        [1]
        """

        if root is None:
            return []
        elements = []
        if root.left:
            elements += self.postorderTraversal(root.left)
        if root.right:
            elements += self.postorderTraversal(root.right)

        elements.append(root.val)
        return elements


if __name__ == "__main__":
    import doctest

    doctest.testmod()
