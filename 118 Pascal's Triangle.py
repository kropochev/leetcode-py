from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Given an integer numRows, return the first numRows of Pascal's triangle.

        In Pascal's triangle, each number is the sum of the two numbers
        directly above it.

        >>> Solution().generate(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        >>> Solution().generate(1)
        [[1]]
        """
        r = [[1]]
        if numRows == 1:
            return r
        r = [[1], [1, 1]]
        if numRows == 2:
            return r
        for i in range(3, numRows + 1):
            t = [1]
            for j in range(1, i-1):
                t.append(r[-1][j - 1] + r[-1][j])
            t.append(1)
            r.append(t)
        return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
