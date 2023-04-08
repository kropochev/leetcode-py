from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        Given a 2D grid consists of 0s (land) and 1s (water).
        An island is a maximal 4-directionally connected group of 0s and
        a closed island is an island totally (all left, top, right, bottom)
        surrounded by 1s.

        Return the number of closed islands.

        >>> Solution().closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]])
        2
        >>> Solution().closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]])
        1
        >>> Solution().closedIsland([[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]])
        2
        """
        m, n = len(grid), len(grid[0])
        count = 0
        visit = [[False for _ in range(n)] for _ in range(m)]

        def dfs(x, y, m, n):
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            if grid[x][y] == 1 or visit[x][y]:
                return True

            visit[x][y] = True
            isClosed = True
            dirx = [0, 1, 0, -1]
            diry = [-1, 0, 1, 0]

            for i in range(4):
                r = x + dirx[i]
                c = y + diry[i]
                if not dfs(r, c, m, n):
                    isClosed = False

            return isClosed

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visit[i][j] and dfs(i, j, m, n):
                    count += 1
        return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
