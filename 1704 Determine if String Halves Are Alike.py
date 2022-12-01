class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """
        You are given a string s of even length. Split this string into two
        halves of equal lengths, and let a be the first half
        and b be the second half.

        Two strings are alike if they have the same number of vowels
        ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
        Notice that s contains uppercase and lowercase letters.

        Return true if a and b are alike. Otherwise, return false.

        >>> Solution().halvesAreAlike("book")
        True
        >>> Solution().halvesAreAlike("textbook")
        False
        """
        v = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        lv, rv = 0, 0
        m = len(s) // 2
        for i in range(m):
            if s[i] in v:
                lv += 1
            if s[m + i] in v:
                rv += 1
        return lv == rv


if __name__ == "__main__":
    import doctest

    doctest.testmod()
