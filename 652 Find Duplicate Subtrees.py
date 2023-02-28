from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        Given the root of a binary tree, return all duplicate subtrees.

        For each kind of duplicate subtrees, you only need to return the root
        node of any one of them.

        Two trees are duplicate if they have the same structure with the same
        node values.

        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(3)
        >>> root.left.left = TreeNode(4)
        >>> root.right.left = TreeNode(2)
        >>> root.right.right = TreeNode(4)
        >>> root.right.left.left = TreeNode(4)
        >>> Solution().findDuplicateSubtrees(root)
        [[TreeNode(2, 4), TreeNode(4)]]
        """
        c = defaultdict(int)
        ans = []

        def inorder(node: TreeNode):
            if not node:
                return ""
            s = '(' + inorder(node.left) + str(node.val) + inorder(node.right) + ')'
            c[s] += 1
            if c[s] == 2:
                ans.append(node)
            return s

        inorder(root)
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
