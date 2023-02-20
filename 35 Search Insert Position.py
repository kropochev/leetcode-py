from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array of distinct integers and a target value,
        return the index if the target is found. If not, return the index where
        it would be if it were inserted in order.
        You must write an algorithm with O(log n) runtime complexity.

        >>> Solution().searchInsert([1,3,5,6], 5)
        2
        >>> Solution().searchInsert([1,3,5,6], 2)
        1
        >>> Solution().searchInsert([1,3,5,6], 7)
        4
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    import doctest

    doctest.testmod()
