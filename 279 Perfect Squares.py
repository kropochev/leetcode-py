from math import sqrt
from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        """
        Given an integer n, return the least number of perfect square numbers
        that sum to n.

        A perfect square is an integer that is the square of an integer;
        in other words, it is the product of some integer with itself.
        For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

        >>> Solution().numSquares(12)
        3
        >>> Solution().numSquares(13)
        2
        """

        def to_sum_of_squares(n: int, k: int) -> List:
            if (n < 0) or (k <= 0):
                return []
            maximum = round(sqrt(n))
            if n == maximum * maximum:
                return [n]
            for c in range(1, maximum + 1):
                decomposition = to_sum_of_squares((n - c * c), k - 1)
                if decomposition:
                    return [c * c] + decomposition

        for k in range(1, 5):
            decompose = to_sum_of_squares(n, k)
            if decompose:
                return len(decompose)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
