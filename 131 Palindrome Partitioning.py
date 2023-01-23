from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Given a string s, partition s such that every substring of
        the partition is a palindrome. Return all possible palindrome
        partitioning of s.

        >>> Solution().partition("aab")
        [['a', 'a', 'b'], ['aa', 'b']]
        >>> Solution().partition("a")
        [['a']]
        """
        def is_palindrome(s):
            return s == s[::-1]

        def backtrack(start, path, res):
            if start == len(s):
                res.append(path)
                return
            for i in range(start, len(s)):
                if is_palindrome(s[start:i+1]):
                    backtrack(i+1, path + [s[start:i+1]], res)

        res = []
        backtrack(0, [], res)
        return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
