from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        You are given an integer array nums. You are initially positioned
        at the array's first index, and each element in the array represents
        your maximum jump length at that position.

        Return true if you can reach the last index, or false otherwise.

        >>> Solution().canJump([2,3,1,1,4])
        True
        >>> Solution().canJump([3,2,1,0,4])
        False
        """
        n = len(nums)
        k = n-1
        for i in range(n-2, -1, -1):
            if nums[i] >= k-i:
                k = i
        return k == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
