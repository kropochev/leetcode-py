from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        You are given the root of a binary tree.

        A ZigZag path for a binary tree is defined as follow:
        - Choose any node in the binary tree and a direction (right or left).
        - If the current direction is right, move to the right child of
        the current node; otherwise, move to the left child.
        - Change the direction from right to left or from left to right.
        - Repeat the second and third steps until you can't move in the tree.
        Zigzag length is defined as the number of nodes visited - 1.
        (A single node has a length of 0).

        Return the longest ZigZag path contained in that tree.

        >>> root = TreeNode(1)
        >>> root.right = TreeNode(1)
        >>> root.right.left = TreeNode(1)
        >>> root.right.right = TreeNode(1)
        >>> root.right.right.left = TreeNode(1)
        >>> root.right.right.right = TreeNode(1)
        >>> root.right.right.left.right = TreeNode(1)
        >>> root.right.right.left.right.right = TreeNode(1)
        >>> Solution().longestZigZag(root)
        3
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(1)
        >>> root.right = TreeNode(1)
        >>> root.left.right = TreeNode(1)
        >>> root.left.right.left = TreeNode(1)
        >>> root.left.right.right = TreeNode(1)
        >>> root.left.right.left.right = TreeNode(1)
        >>> Solution().longestZigZag(root)
        4
        >>> root = TreeNode(1)
        >>> Solution().longestZigZag(root)
        0
        """
        ans = 0

        def dfs(node: Optional[TreeNode], left: bool, steps: int):
            nonlocal ans
            if node:
                ans = max(ans, steps)
                if left:
                    dfs(node.left, False, steps + 1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, steps + 1)

        dfs(root, False, 0)
        dfs(root, True, 0)
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
