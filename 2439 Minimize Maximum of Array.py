from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        """
        You are given a 0-indexed array nums comprising of n non-negative
        integers.

        In one operation, you must:
        - Choose an integer i such that 1 <= i < n and nums[i] > 0.
        - Decrease nums[i] by 1.
        - Increase nums[i - 1] by 1.

        Return the minimum possible value of the maximum integer of nums after
        performing any number of operations.

        >>> Solution().minimizeArrayValue([3,7,1,6])
        5
        >>> Solution().minimizeArrayValue([10,1])
        10
        """
        ans, total = nums[0], nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            ans = max(ans, (total+i)//(i+1))
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
