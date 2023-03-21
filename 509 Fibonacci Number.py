from functools import lru_cache


class Solution:
    @lru_cache
    def fib(self, n: int) -> int:
        """
        The Fibonacci numbers, commonly denoted F(n) form a sequence, called
        the Fibonacci sequence, such that each number is the sum of the two
        preceding ones, starting from 0 and 1. That is,

        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2), for n > 1.
        Given n, calculate F(n).

        >>> Solution().fib(2)
        1
        >>> Solution().fib(3)
        2
        >>> Solution().fib(4)
        3
        """
        if n < 2:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
