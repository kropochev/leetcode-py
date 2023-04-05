from math import dist
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Given an array of points where points[i] = [xi, yi] represents a point
        on the X-Y plane and an integer k, return the k closest points
        to the origin (0, 0).

        The distance between two points on the X-Y plane is the Euclidean
        distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).

        You may return the answer in any order. The answer is guaranteed to be
        unique (except for the order that it is in).

        >>> Solution().kClosest([[1,3],[-2,2]], 1)
        [[-2, 2]]
        >>> Solution().kClosest([[3,3],[5,-1],[-2,4]], 2)
        [[3, 3], [-2, 4]]
        """
        for i in range(len(points)):
            points[i].append(dist(points[i], [0, 0]))
        points.sort(key=lambda x: x[-1])
        return [point[:2] for point in points[:k]]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
