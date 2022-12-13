from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        Given an n x n array of integers matrix, return the minimum sum of any
        falling path through matrix.

        A falling path starts at any element in the first row and chooses
        the element in the next row that is either directly below or diagonally
        left/right. Specifically, the next element from position (row, col)
        will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

        >>> Solution().minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])
        13
        >>> Solution().minFallingPathSum([[-19,57],[-40,-5]])
        -59
        >>> Solution().minFallingPathSum([[-48]])
        -48
        """

        length = len(matrix)
        if length == 1:
            return matrix[0][0]

        for row in range(1, length):
            for i in range(length):
                cur = matrix[row][i]
                mid = matrix[row-1][i]
                if i == 0:
                    matrix[row][i] = cur + min([mid, matrix[row-1][i+1]])
                elif i == length-1:
                    matrix[row][i] = cur + min([mid, matrix[row-1][i-1]])
                else:
                    matrix[row][i] = cur + min([mid, matrix[row-1][i-1], matrix[row-1][i+1]])

        return min(matrix[-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
