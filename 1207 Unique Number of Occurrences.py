from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Given an array of integers arr, return true if the number of
        occurrences of each value in the array is unique, or false otherwise.

        >>> Solution().uniqueOccurrences([1,2,2,1,1,3])
        True
        >>> Solution().uniqueOccurrences([1,2])
        False
        >>> Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
        True
        """
        from collections import Counter
        c = Counter(arr)
        v = c.values()
        return len(v) == len(set(v))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
