from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.answer = -1

    def longestCycle(self, edges: List[int]) -> int:
        """
        You are given a directed graph of n nodes numbered from 0 to n - 1,
        where each node has at most one outgoing edge.

        The graph is represented with a given 0-indexed array edges of size n,
        indicating that there is a directed edge from node i to node edges[i].
        If there is no outgoing edge from node i, then edges[i] == -1.

        Return the length of the longest cycle in the graph. If no cycle exists,
        return -1.

        A cycle is a path that starts and ends at the same node.

        >>> Solution().longestCycle([3,3,4,2,3])
        3
        >>> Solution().longestCycle([2,-1,3,1])
        -1
        """
        def dfs(node: int):
            visited[node] = True
            neighbor = edges[node]
            if neighbor != -1 and not visited[neighbor]:
                dist[neighbor] = dist[node] + 1
                dfs(neighbor)
            elif neighbor != -1 and dist[neighbor]:
                self.answer = max(self.answer, dist[node] - dist[neighbor] + 1)

        visited = [False] * len(edges)
        for i in range(len(edges)):
            dist = defaultdict(int)
            dist[i] = 1
            dfs(i)
        return self.answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
