from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """
        We want to split a group of n people (labeled from 1 to n)
        into two groups of any size. Each person may dislike some other people,
        and they should not go into the same group.

        Given the integer n and the array dislikes where dislikes[i] = [ai, bi]
        indicates that the person labeled ai does not like
        the person labeled bi, return true if it is possible to split everyone
        into two groups in this way.

        >>> Solution().possibleBipartition(4, [[1,2],[1,3],[2,4]])
        True
        >>> Solution().possibleBipartition(3, [[1,2],[1,3],[2,3]])
        False
        >>> Solution().possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]])
        False
        """

        edges = [[] for _ in range(n + 1)]
        for v in dislikes:
            edges[v[0]].append(v[1])
            edges[v[1]].append(v[0])

        color = [-1] * (n + 1)
        queue = []
        for i in range(n):
            if color[i] == -1:
                queue.append([i, 0])
                color[i] = 0
                while queue:
                    v, c = queue.pop(0)
                    for j in edges[v]:
                        if color[j] == c:
                            return False
                        if color[j] == -1:
                            color[j] = 0 if c == 1 else 1
                            queue.append([j, color[j]])

        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
