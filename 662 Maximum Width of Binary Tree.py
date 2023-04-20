from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return the maximum width of
        the given tree.

        The maximum width of a tree is the maximum width among all levels.

        The width of one level is defined as the length between the end-nodes
        (the leftmost and rightmost non-null nodes), where the null nodes
        between the end-nodes that would be present in a complete binary tree
        extending down to that level are also counted into
        the length calculation.

        It is guaranteed that the answer will in the range of a 32-bit signed
        integer.

        >>> root = TreeNode(1)
        >>> root.left = TreeNode(3)
        >>> root.right = TreeNode(2)
        >>> root.left.left = TreeNode(5)
        >>> root.left.right = TreeNode(3)
        >>> root.right.right = TreeNode(9)
        >>> Solution().widthOfBinaryTree(root)
        4
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(3)
        >>> root.right = TreeNode(2)
        >>> root.left.left = TreeNode(5)
        >>> root.left.left.left = TreeNode(6)
        >>> root.right.right = TreeNode(9)
        >>> root.right.right.left = TreeNode(7)
        >>> Solution().widthOfBinaryTree(root)
        7
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(3)
        >>> root.right = TreeNode(2)
        >>> root.left.left = TreeNode(5)
        >>> Solution().widthOfBinaryTree(root)
        2
        """
        def maxWidth(node: Optional[TreeNode], level: int, i: int):
            nonlocal m_min, m_max
            if node is None:
                return
            m_max[level] = max(i, m_max[level]) if level in m_max else i
            m_min[level] = min(i, m_min[level]) if level in m_min else i
            maxWidth(node.left, level + 1, 2 * i + 1)
            maxWidth(node.right, level + 1, 2 * i + 2)

        ans = 0
        m_min, m_max = dict(), dict()
        maxWidth(root, 0, 0)
        for level in m_max.keys():
            ans = max(ans, m_max[level] - m_min[level] + 1)
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
