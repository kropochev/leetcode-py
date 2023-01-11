from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """Given an integer array nums, return the largest perimeter
        of a triangle with a non-zero area, formed from three of these lengths.
        If it is impossible to form any triangle of a non-zero area, return 0.

        >>> Solution().largestPerimeter([2,1,2])
        5
        >>> Solution().largestPerimeter([1,2,1,10])
        0
        """

        nums.sort(reverse=True)
        p = 0
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                p = nums[i] + nums[i+1] + nums[i+2]
                break
        return p


if __name__ == "__main__":
    import doctest

    doctest.testmod()
