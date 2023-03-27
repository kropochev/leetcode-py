from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Given a m x n grid filled with non-negative numbers, find a path from
        top left to bottom right, which minimizes the sum of all numbers along
        its path.

        Note: You can only move either down or right at any point in time.

        >>> Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])
        7
        >>> Solution().minPathSum([[1,2,3],[4,5,6]])
        12
        """
        m = len(grid[0])
        n = len(grid)

        for i in range(n):
            for j in range(m):
                if j != 0 and i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0 and i != 0:
                    grid[i][j] += grid[i - 1][j]
                elif j > 0 and i > 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
