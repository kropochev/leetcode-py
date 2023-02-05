from typing import List
from string import ascii_lowercase


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Given two strings s and p, return an array of all the start indices
        of p's anagrams in s. You may return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters
        of a different word or phrase, typically using all the original letters
        exactly once

        >>> Solution().findAnagrams("cbaebabacd", "abc")
        [0, 6]
        >>> Solution().findAnagrams("abab", "ab")
        [0, 1, 2]
        """

        r = []
        hashS, hashP = {}, {}

        for c in ascii_lowercase:
            hashS[c] = 0
            hashP[c] = 0

        for c in p:
            hashP[c] += 1

        len_s, len_p = len(s), len(p)
        if len_p > len_s:
            return []

        for c in range(0, len_p):
            hashS[s[c]] += 1

        if hashS == hashP:
            r.append(0)

        for i in range(len_p, len_s):
            hashS[s[i-len_p]] -= 1
            hashS[s[i]] += 1

            if hashS == hashP:
                r.append(i-len_p+1)
        return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
