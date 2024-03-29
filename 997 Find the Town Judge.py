from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        In a town, there are n people labeled from 1 to n. There is a rumor
        that one of these people is secretly the town judge.

        If the town judge exists, then:
        - The town judge trusts nobody.
        - Everybody (except for the town judge) trusts the town judge.

        There is exactly one person that satisfies properties 1 and 2.
        You are given an array trust where trust[i] = [ai, bi] representing
        that the person labeled ai trusts the person labeled bi.

        Return the label of the town judge if the town judge exists and
        can be identified, or return -1 otherwise.

        >>> Solution().findJudge(2, [[1,2]])
        2
        >>> Solution().findJudge(3, [[1,3],[2,3]])
        3
        >>> Solution().findJudge(3, [[1,3],[2,3],[3,1]])
        -1
        """
        trusted = [0] * (n+1)
        for u, v in trust:
            trusted[u] -= 1
            trusted[v] += 1

        for i in range(1, n+1):
            if trusted[i] == n-1:
                return i
        else:
            return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
