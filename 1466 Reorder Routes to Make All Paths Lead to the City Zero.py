from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        There are n cities numbered from 0 to n - 1 and n - 1 roads such that
        there is only one way to travel between two different cities
        (this network form a tree). Last year, The ministry of transport
        decided to orient the roads in one direction because
        they are too narrow.

        Roads are represented by connections where connections[i] = [ai, bi]
        represents a road from city ai to city bi.

        This year, there will be a big event in the capital (city 0), and many
        people want to travel to this city.

        Your task consists of reorienting some roads such that each city
        can visit the city 0. Return the minimum number of edges changed.

        It's guaranteed that each city can reach city 0 after reorder.

        >>> Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]])
        3
        >>> Solution().minReorder(5, [[1,0],[1,2],[3,2],[3,4]])
        2
        >>> Solution().minReorder(3, [[1,0],[2,0]])
        0
        """
        count = 0
        adj = defaultdict(list)
        for con in connections:
            adj[con[0]].append([con[1], 1])
            adj[con[1]].append([con[0], 0])

        def dfs(node: int, parent: int):
            nonlocal count
            for child, sign in adj[node]:
                if child != parent:
                    count += sign
                    dfs(child, node)

        dfs(0, -1)
        return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
