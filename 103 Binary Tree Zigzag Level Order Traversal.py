from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Given the root of a binary tree, return the zigzag level order
        traversal of its nodes' values. (i.e., from left to right,
        then right to left for the next level and alternate between).

        >>> root = TreeNode(3)
        >>> root.left = TreeNode(9)
        >>> root.right = TreeNode(20)
        >>> root.right.left = TreeNode(15)
        >>> root.right.right = TreeNode(7)
        >>> Solution().zigzagLevelOrder(root)
        [[3], [20, 9], [15, 7]]
        >>> root = TreeNode(1)
        >>> Solution().zigzagLevelOrder(root)
        [[1]]
        >>> Solution().zigzagLevelOrder(None)
        []
        """
        ans = []
        if root:
            left, right = [], []
            right.append(root)
            while left or right:
                level = []
                while right:
                    tmp = right.pop()
                    level.append(tmp.val)
                    if tmp.left:
                        left.append(tmp.left)
                    if tmp.right:
                        left.append(tmp.right)
                if level:
                    ans.append(level)
                level = []
                while left:
                    tmp = left.pop()
                    level.append(tmp.val)
                    if tmp.right:
                        right.append(tmp.right)
                    if tmp.left:
                        right.append(tmp.left)
                if level:
                    ans.append(level)

        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
