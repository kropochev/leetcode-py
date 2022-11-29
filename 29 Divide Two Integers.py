class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Given two integers dividend and divisor, divide two integers without
        using multiplication, division, and mod operator.

        The integer division should truncate toward zero, which means losing
        its fractional part. For example, 8.345 would be truncated to 8,
        and -2.7335 would be truncated to -2.

        Return the quotient after dividing dividend by divisor.

        Note: Assume we are dealing with an environment that could only store
        integers within the 32-bit signed integer range: [-2^31, 2^31 - 1].
        For this problem, if the quotient is strictly greater than 2^31 - 1,
        then return 2^31 - 1, and if the quotient is strictly less than -2^31,
        then return -2^31.

        >>> Solution().divide(10, 3)
        3
        >>> Solution().divide(7, -3)
        -2
        >>> Solution().divide(-1, -1)
        1
        """
        MIN, MAX = -(2**31), (2**31)-1
        ans = 0
        neg_divident = -1 if dividend < 0 else 1
        neg_divisor = -1 if divisor < 0 else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        for i in range(31, -1, -1):
            if divisor << i <= dividend:
                dividend -= divisor << i
                ans += 1 << i

        r = ans * neg_divident * neg_divisor
        if r < MIN:
            return MIN
        elif r > MAX:
            return MAX
        else:
            return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
