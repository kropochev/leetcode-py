from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        There are some spherical balloons taped onto a flat wall
        that represents the XY-plane. The balloons are represented as
        a 2D integer array points where points[i] = [xstart, xend] denotes
        a balloon whose horizontal diameter stretches between xstart and xend.
        You do not know the exact y-coordinates of the balloons.

        Arrows can be shot up directly vertically (in the positive y-direction)
        from different points along the x-axis. A balloon with xstart and
        xend is burst by an arrow shot at x if xstart <= x <= xend.
        There is no limit to the number of arrows that can be shot. A shot
        arrow keeps traveling up infinitely, bursting any balloons in its path.

        Given the array points, return the minimum number of arrows
        that must be shot to burst all balloons.

        >>> Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])
        2
        >>> Solution().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])
        4
        >>> Solution().findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])
        2
        """
        points = sorted(points, key=lambda x: x[0])
        arrows = 1
        curr = points[0]
        for i in range(1, len(points)):
            if points[i][0] <= curr[1]:
                if points[i][1] < curr[1]:
                    curr[1] = points[i][1]
            else:
                arrows += 1
                curr = points[i]
        return arrows


if __name__ == "__main__":
    import doctest

    doctest.testmod()
