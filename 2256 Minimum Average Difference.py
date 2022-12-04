from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        """
        You are given a 0-indexed integer array nums of length n.

        The average difference of the index i is the absolute difference
        between the average of the first i + 1 elements of nums and the average
        of the last n - i - 1 elements. Both averages should be rounded down
        to the nearest integer.

        Return the index with the minimum average difference.
        If there are multiple such indices, return the smallest one.

        Note:
        - The absolute difference of two numbers is the absolute value
        of their difference.
        - The average of n elements is the sum of the n elements divided
        (integer division) by n.
        - The average of 0 elements is considered to be 0.

        >>> Solution().minimumAverageDifference([2,5,3,9,5,3])
        3
        >>> Solution().minimumAverageDifference([0])
        0
        """
        right_sum = sum(nums)
        left_sum = 0
        min_sum = 2**32
        min_avg = 0
        for i, n in enumerate(nums, start=1):
            right_sum -= n
            left_sum += n
            if i == len(nums):
                avg = sum(nums) // len(nums)
            else:
                avg = abs(left_sum // i - right_sum // (len(nums) - i))
            if avg == 0:
                min_avg = i - 1
                break
            elif avg < min_sum:
                min_sum = avg
                min_avg = i - 1
        return min_avg


if __name__ == "__main__":
    import doctest

    doctest.testmod()
