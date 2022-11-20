from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution,
        and you may not use the same element twice.
        You can return the answer in any order.

        >>> Solution().twoSum([2,7,11,15], 9)
        [0, 1]
        >>> Solution().twoSum([3,2,4], 6)
        [1, 2]
        >>> Solution().twoSum([3,3], 6)
        [0, 1]
        """

        for i, n in enumerate(nums):
            try:
                si = nums.index(target-n, i+1)
                if si > 0:
                    return [i, si]
            except ValueError:
                continue


if __name__ == "__main__":
    import doctest

    doctest.testmod()
