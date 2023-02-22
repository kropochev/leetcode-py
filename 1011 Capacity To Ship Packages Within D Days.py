from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        A conveyor belt has packages that must be shipped from one port
        to another within days days.

        The ith package on the conveyor belt has a weight of weights[i].
        Each day, we load the ship with packages on the conveyor belt
        (in the order given by weights). We may not load more weight than
        the maximum weight capacity of the ship.

        Return the least weight capacity of the ship that will result in all
        the packages on the conveyor belt being shipped within days days.

        >>> Solution().shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)
        15
        >>> Solution().shipWithinDays([3,2,2,4,1,4], 3)
        6
        >>> Solution().shipWithinDays([1,2,3,1,1], 4)
        3
        """
        def check(curr_min):
            days_req = 1
            curr_sum = 0
            for i in range(len(weights)):
                if weights[i] > curr_min:
                    return False
                if curr_sum + weights[i] > curr_min:
                    days_req += 1
                    curr_sum = weights[i]
                    if days_req > days:
                        return False
                else:
                    curr_sum += weights[i]
            return True

        start, end = min(weights), sum(weights)
        result = 0
        while start <= end:
            mid = (start + end) // 2
            if check(mid):
                result = mid
                end = mid - 1
            else:
                start = mid + 1
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
