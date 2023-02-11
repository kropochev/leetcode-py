from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        Given an n x n grid containing only values 0 and 1, where 0 represents
        water and 1 represents land, find a water cell such that its distance
        to the nearest land cell is maximized, and return the distance.
        If no land or water exists in the grid, return -1.

        The distance used in this problem is the Manhattan distance:
        the distance between two cells (x0, y0) and (x1, y1)
        is |x0 - x1| + |y0 - y1|.

        >>> Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]])
        2
        >>> Solution().maxDistance([[1,0,0],[0,0,0],[0,0,0]])
        4
        """
        cols = len(grid[0])
        rows = len(grid)
        queue = list()
        for i in range(cols):
            for j in range(rows):
                if grid[i][j] == 1:
                    queue.append((i, j))

        value = -1
        if not queue or len(queue) == rows * cols:
            return value

        while queue:
            i, j = queue.pop(0)
            value = grid[i][j]
            if i > 0 and grid[i-1][j] == 0:
                queue.append((i-1, j))
                grid[i-1][j] = value + 1
            if i < cols - 1 and grid[i+1][j] == 0:
                queue.append((i+1, j))
                grid[i+1][j] = value + 1
            if j > 0 and grid[i][j-1] == 0:
                queue.append((i, j-1))
                grid[i][j-1] = value + 1
            if j < rows - 1 and grid[i][j+1] == 0:
                queue.append((i, j+1))
                grid[i][j+1] = value + 1

        return value - 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
