class Solution:
    def tribonacci(self, n: int) -> int:
        """
        The Tribonacci sequence Tn is defined as follows:
        T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
        Given n, return the value of Tn.

        >>> Solution().tribonacci(4)
        4
        >>> Solution().tribonacci(25)
        1389537
        """
        d = {0: 0, 1: 1, 2: 1}
        if n < 3:
            return d[n]
        else:
            for i in range(3, n):
                d[i] = d[i-1] + d[i-2] + d[i-3]
            return d[n-1] + d[n-2] + d[n-3]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
