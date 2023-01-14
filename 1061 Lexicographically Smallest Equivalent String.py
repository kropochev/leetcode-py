import string


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        You are given two strings of the same length s1 and s2 and
        a string baseStr.
        We say s1[i] and s2[i] are equivalent characters.

        For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c',
        'b' == 'd', and 'c' == 'e'.
        Equivalent characters follow the usual rules of any equivalence
        relation:
        - Reflexivity: 'a' == 'a'.
        - Symmetry: 'a' == 'b' implies 'b' == 'a'.
        - Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.

        For example, given the equivalency information from s1 = "abc" and
        s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed",
        and "aab" is the lexicographically smallest equivalent string
        of baseStr.

        Return the lexicographically smallest equivalent string of baseStr
        by using the equivalency information from s1 and s2.

        >>> Solution().smallestEquivalentString("parker", "morris", "parser")
        'makkek'
        >>> Solution().smallestEquivalentString("hello", "world", "hold")
        'hdld'
        >>> Solution().smallestEquivalentString("leetcode", "programs", "sourcecode")
        'aauaaaaada'
        """

        d = {c: c for c in string.ascii_lowercase}

        def find(p):
            if d[p] == p:
                return p
            d[p] = find(d[p])
            return d[p]

        def union(x, y):
            px, py = find(x), find(y)
            if px > py:
                d[px] = py
            else:
                d[py] = px

        for x, y in zip(s1, s2):
            union(x, y)

        return ''.join(find(c) for c in baseStr)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
