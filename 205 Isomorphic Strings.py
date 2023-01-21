class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, determine if they are isomorphic.
        Two strings s and t are isomorphic if the characters in s can be
        replaced to get t.
        All occurrences of a character must be replaced with another character
        while preserving the order of characters. No two characters may map
        to the same character, but a character may map to itself.

        >>> Solution().isIsomorphic("egg", "add")
        True
        >>> Solution().isIsomorphic("foo", "bar")
        False
        >>> Solution().isIsomorphic("paper", "title")
        True
        """
        d = dict()
        for i, c in enumerate(s):
            k = d.get(c)
            if k is None:
                if t[i] not in d.values():
                    d[c] = t[i]
                else:
                    return False
            else:
                if k != t[i]:
                    return False
        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
