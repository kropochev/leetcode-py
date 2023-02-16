from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lDepth = self.maxDepth(root.left)
        rDepth = self.maxDepth(root.right)

        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
