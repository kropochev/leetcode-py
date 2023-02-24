import heapq
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """
        You are given an array nums of n positive integers.
        You can perform two types of operations on any element of the array
        any number of times:

        - If the element is even, divide it by 2.
        For example, if the array is [1,2,3,4], then you can do this operation
        on the last element, and the array will be [1,2,3,2].
        - If the element is odd, multiply it by 2.
        For example, if the array is [1,2,3,4], then you can do this operation
        on the first element, and the array will be [2,2,3,4].
        The deviation of the array is the maximum difference between any two
        elements in the array.

        Return the minimum deviation the array can have after performing some
        number of operations.

        >>> Solution().minimumDeviation([1,2,3,4])
        1
        >>> Solution().minimumDeviation([4,1,5,20,3])
        3
        >>> Solution().minimumDeviation([2,10,8])
        3
        """
        arr = []
        min_n, diff = 10**9, 10**9

        for n in nums:
            if n % 2:
                n *= 2
            min_n = min(min_n, n)
            heapq.heappush(arr, -n)

        while arr[0] % 2 == 0:
            max_n = -heapq.heappop(arr)
            diff = min(diff, max_n - min_n)
            min_n = min(min_n, max_n // 2)
            heapq.heappush(arr, -max_n // 2)

        return min(diff, -heapq.heappop(arr) - min_n)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
