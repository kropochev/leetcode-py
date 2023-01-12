from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        Given an undirected tree consisting of n vertices numbered
        from 0 to n-1, which has some apples in their vertices.
        You spend 1 second to walk over one edge of the tree.
        Return the minimum time in seconds you have to spend to collect
        all apples in the tree, starting at vertex 0 and coming back
        to this vertex.

        The edges of the undirected tree are given in the array edges,
        where edges[i] = [ai, bi] means that exists an edge connecting
        the vertices ai and bi. Additionally, there is a boolean array hasApple,
        where hasApple[i] = true means that vertex i has an apple; otherwise,
        it does not have any apple.

        >>> Solution().minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False])
        8
        >>> Solution().minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,False,True,False])
        6
        >>> Solution().minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,False,False,False,False,False])
        0
        """

        def minimumTime(u: int, par: int):
            if hasApple[u]:
                flag[u] = 1
            for it in adj[u]:
                if it != par:
                    minimumTime(it, u)
                    if flag[it] > 0:
                        ans[u] += ans[it] + 2
                    flag[u] |= flag[it]

        adj = [[] for _ in range(n)]
        for i in range(len(edges)):
            source_node = edges[i][0]
            destination_node = edges[i][1]
            adj[source_node].append(destination_node)
            adj[destination_node].append(source_node)

        ans = [0] * len(edges) * 2
        flag = [0] * len(edges) * 2

        minimumTime(0, -1)
        return ans[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
