from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        """
        You are given an array time where time[i] denotes the time taken by
        the ith bus to complete one trip.

        Each bus can make multiple trips successively; that is, the next trip
        can start immediately after completing the current trip. Also, each bus
        operates independently; that is, the trips of one bus do not influence
        the trips of any other bus.

        You are also given an integer totalTrips, which denotes the number
        of trips all buses should make in total. Return the minimum time
        required for all buses to complete at least totalTrips trips.

        >>> Solution().minimumTime([1,2,3], 5)
        3
        >>> Solution().minimumTime([2], 1)
        2
        """
        left, right = 1, max(time)*totalTrips

        def timeEnough(given_time):
            act = 0
            for t in time:
                act += given_time // t
            return act >= totalTrips

        while left < right:
            mid = (left + right) // 2
            if timeEnough(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    import doctest

    doctest.testmod()
