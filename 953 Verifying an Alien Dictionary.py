from typing import List
from collections import defaultdict


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        In an alien language, surprisingly, they also use English lowercase
        letters, but possibly in a different order. The order of the alphabet
        is some permutation of lowercase letters.

        Given a sequence of words written in the alien language, and the order
        of the alphabet, return true if and only if the given words are sorted
        lexicographically in this alien language.

        >>> Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
        True
        >>> Solution().isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")
        False
        >>> Solution().isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")
        False
        """
        def helper(first: str, second: str) -> bool:
            for i in range(min(len(first), len(second))):
                if lang[first[i]] != lang[second[i]]:
                    return lang[first[i]] < lang[second[i]]
            return len(first) <= len(second)

        lang = defaultdict(int)
        for i, c in enumerate(order):
            lang[c] = i
        for i in range(len(words)-1):
            if not helper(words[i], words[i+1]):
                return False
        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
