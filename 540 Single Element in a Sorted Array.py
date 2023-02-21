from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        You are given a sorted array consisting of only integers where every
        element appears exactly twice, except for one element which appears
        exactly once.

        Return the single element that appears only once.

        Your solution must run in O(log n) time and O(1) space.

        >>> Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8])
        2
        >>> Solution().singleNonDuplicate([3,3,7,7,10,11,11])
        10
        """
        if len(nums) == 1:
            return nums[0]
        elif nums[-1] > nums[-2]:
            return nums[-1]
        elif nums[0] < nums[1]:
            return nums[0]

        def find(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid-1] < nums[mid] < nums[mid+1]:
                    return nums[mid]
                return find(left, mid-1) or find(mid+1, right)

        return find(1, len(nums) - 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
