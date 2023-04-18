from itertools import chain, zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        You are given two strings word1 and word2. Merge the strings by adding
        letters in alternating order, starting with word1.
        If a string is longer than the other, append the additional letters
        onto the end of the merged string.

        Return the merged string.

        >>> Solution().mergeAlternately('abc', 'pqr')
        'apbqcr'
        >>> Solution().mergeAlternately('ab', 'pqrs')
        'apbqrs'
        >>> Solution().mergeAlternately('abcd', 'pq')
        'apbqcd'
        """
        return ''.join(chain(x + y for x, y in zip_longest(word1, word2, fillvalue='')))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
