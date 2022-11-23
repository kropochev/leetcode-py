from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        """
        An n x n matrix is valid if every row and every column contains all
        the integers from 1 to n (inclusive).

        Given an n x n integer matrix matrix, return true if the matrix
        is valid. Otherwise, return false.

        >>> Solution().checkValid([[1,2,3],[3,1,2],[2,3,1]])
        True
        >>> Solution().checkValid([[1,1,1],[1,2,3],[1,2,3]])
        False
        """
        def isTrue(n: List) -> bool:
            return len(n) == len(set(n))

        for row in matrix:
            if not isTrue(row):
                return False

        for col in zip(*matrix):
            if not isTrue(col):
                return False

        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
