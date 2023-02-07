from typing import List
from math import dist


class Solution:
    def countPoints(
        self, points: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        """
        You are given an array points where points[i] = [xi, yi]
        is the coordinates of the ith point on a 2D plane. Multiple points
        can have the same coordinates.

        You are also given an array queries where queries[j] = [xj, yj, rj]
        describes a circle centered at (xj, yj) with a radius of rj.

        For each query queries[j], compute the number of points inside the jth
        circle. Points on the border of the circle are considered inside.

        Return an array answer, where answer[j] is the answer to the jth query.

        >>> Solution().countPoints([[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]])
        [3, 2, 2]
        >>> Solution().countPoints([[1,1],[2,2],[3,3],[4,4],[5,5]], [[1,2,2],[2,2,2],[4,3,2],[4,3,3]])
        [2, 3, 2, 4]
        """
        ans = []
        for *q, r in queries:
            c = 0
            for p in points:
                if dist(p, q) <= r:
                    c += 1
            ans.append(c)
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
