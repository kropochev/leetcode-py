from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """
        An image is represented by an m x n integer grid image where
        image[i][j] represents the pixel value of the image.

        You are also given three integers sr, sc, and color. You should perform
        a flood fill on the image starting from the pixel image[sr][sc].

        To perform a flood fill, consider the starting pixel, plus any pixels
        connected 4-directionally to the starting pixel of the same color as
        the starting pixel, plus any pixels connected 4-directionally
        to those pixels (also with the same color), and so on.
        Replace the color of all of the aforementioned pixels with color.

        Return the modified image after performing the flood fill.

        >>> Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
        [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        >>> Solution().floodFill([[0,0,0],[0,0,0]], 0, 0, 0)
        [[0, 0, 0], [0, 0, 0]]
        >>> Solution().floodFill([[0,0,0],[0,0,0]], 1, 0, 2)
        [[2, 2, 2], [2, 2, 2]]
        """

        def colorize(sr: int, sc: int, tc: int, color: int) -> None:
            r = len(image)-1
            c = len(image[0])-1

            if image[sr][sc] == tc:
                image[sr][sc] = color

                if sc > 0:
                    colorize(sr, sc-1, tc, color)
                if sc < c:
                    colorize(sr, sc+1, tc, color)
                if sr > 0:
                    colorize(sr-1, sc, tc, color)
                if sr < r:
                    colorize(sr+1, sc, tc, color)

        tc = image[sr][sc]
        if tc != color:
            colorize(sr, sc, tc, color)
        return image


if __name__ == "__main__":
    import doctest

    doctest.testmod()
