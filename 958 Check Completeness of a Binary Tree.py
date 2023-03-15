from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """
        Given the root of a binary tree, determine if it is a complete
        binary tree.

        In a complete binary tree, every level, except possibly the last,
        is completely filled, and all nodes in the last level are as far left
        as possible. It can have between 1 and 2^h nodes
        inclusive at the last level h.

        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(3)
        >>> root.left.left = TreeNode(4)
        >>> root.left.right = TreeNode(5)
        >>> root.right.left = TreeNode(6)
        >>> Solution().isCompleteTree(root)
        True
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(3)
        >>> root.left.left = TreeNode(4)
        >>> root.left.right = TreeNode(5)
        >>> root.right.right = TreeNode(7)
        >>> Solution().isCompleteTree(root)
        False
        """

        if root is None:
            return True

        q = []
        q.append(root)
        flag = False

        while len(q) > 0:
            temp = q.pop(0)

            if temp is None:
                flag = True
            else:
                if flag:
                    return False
                q.append(temp.left)
                q.append(temp.right)

        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
