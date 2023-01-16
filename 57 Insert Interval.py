from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        You are given an array of non-overlapping intervals intervals where
        intervals[i] = [start_i, end_i] represent the start and the end
        of the ith interval and intervals is sorted in ascending order
        by start_i. You are also given an interval newInterval = [start, end]
        that represents the start and end of another interval.

        Insert newInterval into intervals such that intervals is still sorted
        in ascending order by starti and intervals still does not have any
        overlapping intervals (merge overlapping intervals if necessary).

        Return intervals after the insertion.

        >>> Solution().insert([[1,3],[6,9]], [2,5])
        [[1, 5], [6, 9]]
        >>> Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
        [[1, 2], [3, 10], [12, 16]]
        """
        start, end = newInterval

        def bs_rightedge(x, left, right):
            left = left
            right = right
            rt_edge = right + 1

            while left <= right:
                mid = (left + right) // 2
                if intervals[mid][0] > x:
                    rt_edge = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return rt_edge

        def bs_leftedge(x, left, right):
            left = left
            right = right
            lt_edge = left - 1

            while left <= right:
                mid = (left + right) // 2
                if intervals[mid][1] < x:
                    lt_edge = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return lt_edge

        rt_edge = bs_rightedge(end, 0, len(intervals) - 1)
        lt_edge = bs_leftedge(start, 0, rt_edge - 1)

        if (rt_edge - lt_edge) > 1:
            start = min(start, intervals[lt_edge + 1][0])
            end = max(end, intervals[rt_edge - 1][1])
        return intervals[: lt_edge + 1] + [[start, end]] + intervals[rt_edge:]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
