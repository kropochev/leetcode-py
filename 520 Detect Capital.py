class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        We define the usage of capitals in a word to be right when one of
        the following cases holds:
        - All letters in this word are capitals, like "USA".
        - All letters in this word are not capitals, like "leetcode".
        - Only the first letter in this word is capital, like "Google".

        Given a string word, return true if the usage of capitals
        in it is right.

        >>> Solution().detectCapitalUse("USA")
        True
        >>> Solution().detectCapitalUse("FlaG")
        False
        >>> Solution().detectCapitalUse("leetcode")
        True
        >>> Solution().detectCapitalUse("Google")
        True
        >>> Solution().detectCapitalUse("leetCode")
        False
        """
        return word.istitle() or word.isupper() or word.islower()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
