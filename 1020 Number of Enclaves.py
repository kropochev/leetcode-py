from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        You are given an m x n binary matrix grid, where 0 represents a sea
        cell and 1 represents a land cell.

        A move consists of walking from one land cell to another adjacent
        (4-directionally) land cell or walking off the boundary of the grid.

        Return the number of land cells in grid for which we cannot walk off
        the boundary of the grid in any number of moves.

        >>> Solution().numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
        3
        >>> Solution().numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]])
        0
        """
        m, n = len(grid), len(grid[0])
        count = 0
        visit = [[False for _ in range(n)] for _ in range(m)]

        def dfs(x, y, m, n):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0 or visit[x][y]:
                return

            visit[x][y] = True
            dirx = [0, 1, 0, -1]
            diry = [-1, 0, 1, 0]

            for i in range(4):
                dfs(x + dirx[i], y + diry[i], m, n)

        for i in range(m):
            if grid[i][0] == 1 and not visit[i][0]:
                dfs(i, 0, m, n)
            if grid[i][n - 1] == 1 and not visit[i][n - 1]:
                dfs(i, n - 1, m, n)

        for i in range(n):
            if grid[0][i] == 1 and not visit[0][i]:
                dfs(0, i, m, n)
            if grid[m - 1][i] == 1 and not visit[m - 1][i]:
                dfs(m - 1, i, m, n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visit[i][j]:
                    count += 1

        return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
