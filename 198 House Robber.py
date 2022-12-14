from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        You are a professional robber planning to rob houses along a street.
        Each house has a certain amount of money stashed, the only constraint
        stopping you from robbing each of them is that adjacent houses have
        security systems connected and it will automatically contact the police
        if two adjacent houses were broken into on the same night.

        Given an integer array nums representing the amount of money of each
        house, return the maximum amount of money you can rob tonight without
        alerting the police.

        >>> Solution().rob([1,2,3,1])
        4
        >>> Solution().rob([2,7,9,3,1])
        12
        """

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        nums[1] = max(nums[0], nums[1])
        for i in range(2, n):
            nums[i] = max(nums[i-2] + nums[i], nums[i-1])

        return max(nums[n-2], nums[n-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
