class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        A binary string is monotone increasing if it consists of some number
        of 0's (possibly none), followed by some number of 1's
        (also possibly none).

        You are given a binary string s. You can flip s[i] changing it
        from 0 to 1 or from 1 to 0.

        Return the minimum number of flips to make s monotone increasing.

        >>> Solution().minFlipsMonoIncr("00110")
        1
        >>> Solution().minFlipsMonoIncr("010110")
        2
        >>> Solution().minFlipsMonoIncr("00011000")
        2
        """

        countFlip, countOne = 0, 0
        for c in s:
            if c == '1':
                countOne += 1
            else:
                countFlip += 1
                countFlip = min(countFlip, countOne)
        return countFlip


if __name__ == "__main__":
    import doctest

    doctest.testmod()
