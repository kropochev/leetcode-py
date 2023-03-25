from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        """
        You are given an integer n. There is an undirected graph with n nodes,
        numbered from 0 to n - 1. You are given a 2D integer array edges where
        edges[i] = [ai, bi] denotes that there exists an undirected edge
        connecting nodes ai and bi.

        Return the number of pairs of different nodes that are unreachable from
        each other.

        >>> Solution().countPairs(3, [[0,1],[0,2],[1,2]])
        0
        >>> Solution().countPairs(7, [[0,2],[0,5],[2,4],[1,6],[5,4]])
        14
        """

        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(node):
            count = 1
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    count += dfs(neighbor)
            return count

        result = 0
        count = 0
        remaining = n
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                count = dfs(i)
                result += count * (remaining - count)
                remaining -= count
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
