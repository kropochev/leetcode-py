from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Given two integer arrays inorder and postorder where inorder is
        the inorder traversal of a binary tree and postorder is the postorder
        traversal of the same tree, construct and return the binary tree.

        >>> Solution().buildTree([9,3,15,20,7], [9,15,7,20,3])
        >>> Solution().buildTree([-1], [-1])
        """
        st = []
        set = []
        n = len(inorder)
        root = None
        p = n - 1
        i = n - 1

        while p >= 0:
            node = None
            while True:
                node = TreeNode(postorder[p])
                if root is None:
                    root = node
                if len(st) > 0:
                    if st[-1] in set:
                        set.remove(st[-1])
                        st[-1].left = node
                        st.pop()
                    else:
                        st[-1].right = node
                st.append(node)
                p -= 1
                if postorder[p + 1] == inorder[i] or p < 0:
                    break

            node = None
            while len(st) > 0 and i >= 0 and st[-1].val == inorder[i]:
                node = st[-1]
                st.pop()
                i -= 1

            if node is not None:
                set.append(node)
                st.append(node)

        return root


if __name__ == "__main__":
    import doctest

    doctest.testmod()
