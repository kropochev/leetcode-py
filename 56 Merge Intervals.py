from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Given an array of intervals where intervals[i] = [starti, endi],
        merge all overlapping intervals, and return an array of
        the non-overlapping intervals that cover all the intervals in the input.

        >>> Solution().merge([[1,3],[2,6],[8,10],[15,18]])
        [[1, 6], [8, 10], [15, 18]]
        >>> Solution().merge([[1,4],[4,5]])
        [[1, 5]]
        """
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                if intervals[i][1] > ans[-1][1]:
                    ans[-1][1] = intervals[i][1]
            else:
                ans.append(intervals[i])
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
