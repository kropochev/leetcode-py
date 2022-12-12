class Solution:
    def climbStairs(self, n: int) -> int:
        """
        You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways
        can you climb to the top?

        >>> Solution().climbStairs(2)
        2
        >>> Solution().climbStairs(3)
        3
        """
        s = {}

        def fib(n: int, s: dict) -> int:
            if n < 4:
                return n
            if n in s.keys():
                return s[n]

            s[n] = fib(n-1, s) + fib(n-2, s)
            return s[n]

        return fib(n, s)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
