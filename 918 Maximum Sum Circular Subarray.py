from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Given a circular integer array nums of length n, return the maximum
        possible sum of a non-empty subarray of nums.

        A circular array means the end of the array connects to the beginning
        of the array. Formally, the next element of nums[i] is nums[(i + 1) % n]
        and the previous element of nums[i] is nums[(i - 1 + n) % n].

        A subarray may only include each element of the fixed buffer nums
        at most once. Formally, for a subarray nums[i],
        nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j
        with k1 % n == k2 % n.

        >>> Solution().maxSubarraySumCircular([1,-2,3,-2])
        3
        >>> Solution().maxSubarraySumCircular([5,-3,5])
        10
        >>> Solution().maxSubarraySumCircular([-3,-2,-3])
        -2
        """

        n = len(nums)
        if n == 1:
            return nums[0]
    
        sum_nums = sum(nums)

        curr_max = nums[0]
        max_so_far = nums[0]
        curr_min = nums[0]
        min_so_far = nums[0]

        for i in range(1, n):
            curr_max = max(curr_max + nums[i], nums[i])
            max_so_far = max(max_so_far, curr_max)

            curr_min = min(curr_min + nums[i], nums[i])
            min_so_far = min(min_so_far, curr_min)
        if min_so_far == sum_nums:
            return max_so_far

        return max(max_so_far, sum_nums - min_so_far)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
