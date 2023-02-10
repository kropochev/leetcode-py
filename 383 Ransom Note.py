from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Given two strings ransomNote and magazine, return true if ransomNote
        can be constructed by using the letters from magazine and
        false otherwise.

        Each letter in magazine can only be used once in ransomNote.

        >>> Solution().canConstruct("a", "b")
        False
        >>> Solution().canConstruct("aa", "ab")
        False
        >>> Solution().canConstruct("aa", "aab")
        True
        """
        c = Counter(magazine)
        c.subtract(Counter(ransomNote))
        return min(c.values()) >= 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
