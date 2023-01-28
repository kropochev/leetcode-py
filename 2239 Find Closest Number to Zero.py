from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        """
        Given an integer array nums of size n, return the number with the value
        closest to 0 in nums. If there are multiple answers, return the number
        with the largest value.

        >>> Solution().findClosestNumber([-4,-2,1,4,8])
        1
        >>> Solution().findClosestNumber([2,-1,1])
        1
        """
        nums.sort()
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                if nums[i] <= abs(prev):
                    return nums[i]
                else:
                    return prev
            else:
                prev = nums[i]
        return nums[-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
