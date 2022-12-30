from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
        find all possible paths from node 0 to node n - 1 and
        return them in any order.

        The graph is given as follows: graph[i] is a list of all nodes
        you can visit from node i (i.e., there is a directed edge
        from node i to node graph[i][j]).

        >>> Solution().allPathsSourceTarget([[1,2],[3],[3],[]])
        [[0, 1, 3], [0, 2, 3]]
        >>> Solution().allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])
        [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
        """
        def dfs(path: List, node: int):
            if node == nodes-1:
                ans.append(path)
                return
            for i in graph[node]:
                dfs(path + [i], i)

        nodes = len(graph)
        ans = []
        dfs([0], 0)
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
