from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Given a non-negative integer c, decide whether there're
        two integers a and b such that a^2 + b^2 = c.

        >>> Solution().judgeSquareSum(5)
        True
        >>> Solution().judgeSquareSum(3)
        False
        """
        lo = 0
        hi = int(sqrt(c))
        while lo <= hi:
            s = lo**2 + hi**2
            if s == c:
                return True
            if s < c:
                lo += 1
            else:
                hi -= 1
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
