from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given an m x n 2D binary grid grid which represents a map
        of '1's (land) and '0's (water), return the number of islands.

        An island is surrounded by water and is formed by connecting adjacent
        lands horizontally or vertically. You may assume all four edges
        of the grid are all surrounded by water.

        >>> Solution().numIslands(
        ...    [
        ...        ["1", "1", "1", "1", "0"],
        ...        ["1", "1", "0", "1", "0"],
        ...        ["1", "1", "0", "0", "0"],
        ...        ["0", "0", "0", "0", "0"],
        ...    ]
        ... )
        1
        >>> Solution().numIslands(
        ...    [
        ...        ["1", "1", "0", "0", "0"],
        ...        ["1", "1", "0", "0", "0"],
        ...        ["0", "0", "1", "0", "0"],
        ...        ["0", "0", "0", "1", "1"],
        ...    ]
        ... )
        3
        """
        def colorize(sr: int, sc: int, color: str) -> None:
            r = len(grid)-1
            c = len(grid[0])-1

            if grid[sr][sc] == "1":
                grid[sr][sc] = color

                if sc > 0:
                    colorize(sr, sc-1, color)
                if sc < c:
                    colorize(sr, sc+1, color)
                if sr > 0:
                    colorize(sr-1, sc, color)
                if sr < r:
                    colorize(sr+1, sc, color)

        n = 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    n += 1
                    colorize(r, c, str(n))

        return n-1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
