class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        Given a string columnTitle that represents the column title as appears
        in an Excel sheet, return its corresponding column number.

        >>> Solution().titleToNumber("A")
        1
        >>> Solution().titleToNumber("AB")
        28
        >>> Solution().titleToNumber("ZY")
        701
        """
        ans = 0
        for e, c in enumerate(reversed(columnTitle)):
            ans += (ord(c) - 64) * 26 ** e
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
