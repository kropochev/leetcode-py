class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Given two strings needle and haystack, return the index of the first
        occurrence of needle in haystack, or -1 if needle is not part of
        haystack.

        >>> Solution().strStr("sadbutsad", "sad")
        0
        >>> Solution().strStr("leetcode", "leeto")
        -1
        """
        h = len(haystack)
        n = len(needle)
        for i in range(h-n+1):
            for j in range(n):
                if needle[j] != haystack[i + j]:
                    break
                if j == n - 1:
                    return i
        return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
