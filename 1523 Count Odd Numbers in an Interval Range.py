class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        Given two non-negative integers low and high. Return the count of odd
        numbers between low and high (inclusive).

        >>> Solution().countOdds(3, 7)
        3
        >>> Solution().countOdds(8, 10)
        1
        """
        low = low + 1 if low % 2 == 0 else low
        high = high - 1 if high % 2 == 0 else high
        return (high - low) // 2 + 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
