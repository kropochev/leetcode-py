from typing import List
from itertools import combinations


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
        You are given an array of strings arr. A string s is formed by the
        concatenation of a subsequence of arr that has unique characters.

        Return the maximum possible length of s.

        A subsequence is an array that can be derived from another array
        by deleting some or no elements without changing the order
        of the remaining elements.

        >>> Solution().maxLength(["un","iq","ue"])
        4
        >>> Solution().maxLength(["cha","r","act","ers"])
        6
        """
        m = 0
        for i in range(len(arr), 0, -1):
            for c in combinations(arr, i):
                s = "".join(e for e in c)
                length = len(s)
                if length == len(set(s)) and length > m:
                    m = length
        return m


if __name__ == "__main__":
    import doctest

    doctest.testmod()
