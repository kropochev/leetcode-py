from typing import List
from collections import defaultdict


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        """
        There is a bi-directional graph with n vertices, where each vertex
        is labeled from 0 to n - 1 (inclusive). The edges in the graph
        are represented as a 2D integer array edges,
        where each edges[i] = [ui, vi] denotes a bi-directional edge between
        vertex ui and vertex vi. Every vertex pair is connected
        by at most one edge, and no vertex has an edge to itself.

        You want to determine if there is a valid path that exists from vertex
        source to vertex destination.

        Given edges and the integers n, source, and destination, return true
        if there is a valid path from source to destination or false otherwise.

        >>> Solution().validPath(3, [[0,1],[1,2],[2,0]], 0, 2)
        True
        >>> Solution().validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)
        False
        """
        graph = defaultdict(set)
        [(graph[e[0]].add(e[1]), graph[e[1]].add(e[0])) for e in edges]
        visited = [False] * n
        queue = []

        queue.append(source)
        visited[source] = True

        while queue:
            v = queue.pop(0)
            if v == destination:
                return True
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
