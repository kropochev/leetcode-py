from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        """
        Given a n * n matrix grid of 0's and 1's only. We want to represent
        the grid with a Quad-Tree.

        Return the root of the Quad-Tree representing the grid.

        Notice that you can assign the value of a node to True or False when
        isLeaf is False, and both are accepted in the answer.

        A Quad-Tree is a tree data structure in which each internal node
        has exactly four children. Besides, each node has two attributes:
        - val: True if the node represents a grid of 1's or False if the node
        represents a grid of 0's.
        - isLeaf: True if the node is leaf node on the tree or False if the node
        has the four children.

        We can construct a Quad-Tree from a two-dimensional area using
        the following steps:
        - If the current grid has the same value (i.e all 1's or all 0's)
        set isLeaf True and set val to the value of the grid and set
        the four children to Null and stop.
        - If the current grid has different values, set isLeaf to False and set
        val to any value and divide the current grid into four sub-grids as
        shown in the photo.
        - Recurse for each of the children with the proper sub-grid.

        Quad-Tree format:
        The output represents the serialized format of a Quad-Tree using level
        order traversal, where null signifies a path terminator where no node
        exists below.
        It is very similar to the serialization of the binary tree.
        The only difference is that the node is represented as
        a list [isLeaf, val].
        If the value of isLeaf or val is True we represent it as 1 in the list
        [isLeaf, val] and if the value of isLeaf or val is False
        we represent it as 0.

        >>> Solution().construct([[0,1],[1,0]])
        >>> Solution().construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])
        """
        def isLeaf(x: int, y: int, length: int) -> bool:
            for i in range(x, x + length):
                for j in range(y, y + length):
                    if grid[i][j] != grid[x][y]:
                        return False
            return True

        def solve(x: int, y: int, length: int) -> Node:
            if isLeaf(x, y, length):
                return Node(grid[x][y] == 1, True, None, None, None, None)

            root = Node(False, False, None, None, None, None)
            root.topLeft = solve(x, y, length//2)
            root.topRight = solve(x, y + length//2, length//2)
            root.bottomLeft = solve(x + length//2, y, length//2)
            root.bottomRight = solve(x + length//2, y + length//2, length//2)
            return root

        return solve(0, 0, len(grid))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
