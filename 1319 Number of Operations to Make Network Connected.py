from collections import defaultdict
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        There are n computers numbered from 0 to n - 1 connected by ethernet
        cables connections forming a network where connections[i] = [ai, bi]
        represents a connection between computers ai and bi. Any computer can
        reach any other computer directly or indirectly through the network.

        You are given an initial computer network connections. You can extract
        certain cables between two directly connected computers, and place them
        between any pair of disconnected computers to make them directly
        connected.

        Return the minimum number of times you need to do this in order to make
        all the computers connected. If it is not possible, return -1.

        >>> Solution().makeConnected(4, [[0,1],[0,2],[1,2]])
        1
        >>> Solution().makeConnected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]])
        2
        >>> Solution().makeConnected(6, [[0,1],[0,2],[0,3],[1,2]])
        -1
        """
        if len(connections) < n-1:
            return -1

        count = 0
        visited = [False] * n
        adj = defaultdict(list)
        for connection in connections:
            adj[connection[0]].append(connection[1])
            adj[connection[1]].append(connection[0])

        def dfs(node: int):
            visited[node] = True
            for con in adj[node]:
                if not visited[con]:
                    dfs(con)

        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)

        return count - 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
