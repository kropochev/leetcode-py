import math


class Solution:
    def mySqrt(self, x: int) -> int:
        """Given a non-negative integer x, compute and return the square root of x.
        Since the return type is an integer, the decimal digits are truncated,
        and only the integer part of the result is returned.
        Note: You are not allowed to use any built-in exponent function or
        operator, such as pow(x, 0.5) or x ** 0.5.

        >>> Solution().mySqrt(4)
        2
        >>> Solution().mySqrt(8)
        2
        """

        n = 1
        while True:
            nx = (n + x / n) / 2
            if abs(n - nx) < 1e-10:
                break
            n = nx
        return math.trunc(n)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
