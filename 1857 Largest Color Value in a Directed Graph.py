from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
        There is a directed graph of n colored nodes and m edges.
        The nodes are numbered from 0 to n - 1.

        You are given a string colors where colors[i] is a lowercase English
        letter representing the color of the ith node in this graph (0-indexed).
        You are also given a 2D array edges where edges[j] = [aj, bj] indicates
        that there is a directed edge from node aj to node bj.

        A valid path in the graph is a sequence of nodes
        x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge
        from xi to xi+1 for every 1 <= i < k. The color value of the path
        is the number of nodes that are colored the most frequently occurring
        color along that path.

        Return the largest color value of any valid path in the given graph,
        or -1 if the graph contains a cycle.

        >>> Solution().largestPathValue("abaca", [[0,1],[0,2],[2,3],[3,4]])
        3
        >>> Solution().largestPathValue("a", [[0,0]])
        -1
        """

        def dfs(node: int) -> int:
            if inStack[node]:
                return float("inf")
            if visit[node]:
                return count[node][ord(colors[node]) - ord("a")]

            visit[node] = True
            inStack[node] = True

            for neibhor in adj[node]:
                if dfs(neibhor) == float("inf"):
                    return float("inf")
                for i in range(26):
                    count[node][i] = max(count[node][i], count[neibhor][i])

            count[node][ord(colors[node]) - ord("a")] += 1
            inStack[node] = False
            return count[node][ord(colors[node]) - ord("a")]

        n = len(colors)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)

        count = [[0 for _ in range(26)] for _ in range(n)]
        visit = [False for _ in range(n)]
        inStack = [False for _ in range(n)]
        answer = 0
        for i in range(n):
            answer = max(answer, dfs(i))
        return -1 if answer == float("inf") else answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
