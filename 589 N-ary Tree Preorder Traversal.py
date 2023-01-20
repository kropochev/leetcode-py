from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """
        Given the root of an n-ary tree, return the preorder traversal of its
        nodes' values.

        Nary-Tree input serialization is represented in their level order
        traversal. Each group of children is separated by the null value.
        """
        result = []
        nodes = []
        if root is None:
            return result
        nodes.append(root)
        while len(nodes):
            curr = nodes[0]
            nodes.pop()
            result.append(curr.val)
            for it in range(len(curr.children)-1, -1, -1):
                nodes.insert(0, curr.children[it])
        return result
