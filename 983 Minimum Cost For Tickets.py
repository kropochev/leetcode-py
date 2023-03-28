import functools
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        You have planned some train traveling one year in advance. The days of
        the year in which you will travel are given as an integer array days.
        Each day is an integer from 1 to 365.

        Train tickets are sold in three different ways:
        - a 1-day pass is sold for costs[0] dollars,
        - a 7-day pass is sold for costs[1] dollars, and
        - a 30-day pass is sold for costs[2] dollars.

        The passes allow that many days of consecutive travel.
        - For example, if we get a 7-day pass on day 2, then we can travel
        for 7 days: 2, 3, 4, 5, 6, 7, and 8.

        Return the minimum number of dollars you need to travel every day in
        the given list of days.

        >>> Solution().mincostTickets([1,4,6,7,8,20], [2,7,15])
        11
        >>> Solution().mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15])
        17
        """
        @functools.cache
        def dp(index: int) -> int:
            if index > 365:
                return 0
            if index not in days:
                return dp(index + 1)
            return min(
                costs[0] + dp(index + 1),
                costs[1] + dp(index + 7),
                costs[2] + dp(index + 30),
            )
        return dp(1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
