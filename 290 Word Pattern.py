class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Given a pattern and a string s, find if s follows the same pattern.

        Here follow means a full match, such that there is a bijection between
        a letter in pattern and a non-empty word in s.

        >>> Solution().wordPattern("abba", "dog cat cat dog")
        True
        >>> Solution().wordPattern("abba", "dog cat cat fish")
        False
        >>> Solution().wordPattern("aaaa", "dog cat cat dog")
        False
        """
        hash = dict()
        string = s.split()
        if len(pattern) != len(string):
            return False
        for k, v in zip(pattern, string):
            if k in hash.keys():
                if hash[k] == v:
                    continue
                else:
                    return False
            else:
                if v in hash.values():
                    return False
                else:
                    hash[k] = v
        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
