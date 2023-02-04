class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Given two strings s1 and s2, return true if s2 contains a permutation
        of s1, or false otherwise.

        In other words, return true if one of s1's permutations
        is the substring of s2.

        >>> Solution().checkInclusion("ab", "eidbaooo")
        True
        >>> Solution().checkInclusion("ab", "eidboaoo")
        False
        """
        h1 = {chr(c): 0 for c in range(97, 123)}
        h2 = h1.copy()
        l1, l2 = len(s1), len(s2)

        if l1 > l2:
            return False

        for c in s1:
            h1[c] += 1

        for i in range(l1):
            h2[s2[i]] += 1

        if h1 == h2:
            return True

        for i in range(l1, l2):
            h2[s2[i]] += 1
            h2[s2[i-l1]] -= 1
            if h1 == h2:
                return True
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
