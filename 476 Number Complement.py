class Solution:
    def findComplement(self, num: int) -> int:
        """
        The complement of an integer is the integer you get when you flip all
        the 0's to 1's and all the 1's to 0's in its binary representation.

        For example, The integer 5 is "101" in binary and its complement
        is "010" which is the integer 2.
        Given an integer num, return its complement.

        >>> Solution().findComplement(5)
        2
        >>> Solution().findComplement(1)
        0
        """
        c, n = 0, num
        while n:
            c += 1
            n >>= 1
        return num ^ 2**c - 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
