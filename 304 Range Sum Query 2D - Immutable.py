from typing import List


class NumMatrix:
    """
    Given a 2D matrix matrix, handle multiple queries of the following type:
    - Calculate the sum of the elements of matrix inside the rectangle defined
    by its upper left corner (row1, col1) and lower right corner (row2, col2).

    Implement the NumMatrix class:
    - NumMatrix(int[][] matrix) Initializes the object with the integer matrix
    matrix.
    - int sumRegion(int row1, int col1, int row2, int col2) Returns the sum
    of the elements of matrix inside the rectangle defined by its upper left
    corner (row1, col1) and lower right corner (row2, col2).

    You must design an algorithm where sumRegion works on O(1) time complexity.

    >>> m = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
    >>> m.sumRegion(2,1,4,3)
    8
    >>> m.sumRegion(1,1,2,2)
    11
    >>> m.sumRegion(1,2,2,4)
    12
    """

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.dp = [
            [0 for _ in range(cols + 1)] for _ in range(rows + 1)
        ]
        for r in range(rows):
            for c in range(cols):
                self.dp[r + 1][c + 1] = (
                    self.dp[r + 1][c]
                    + self.dp[r][c + 1]
                    + matrix[r][c]
                    - self.dp[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.dp[row2 + 1][col2 + 1]
            - self.dp[row1][col2 + 1]
            - self.dp[row2 + 1][col1]
            + self.dp[row1][col1]
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
