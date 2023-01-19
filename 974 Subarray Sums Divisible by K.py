from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        Given an integer array nums and an integer k, return the number
        of non-empty subarrays that have a sum divisible by k.

        A subarray is a contiguous part of an array.

        >>> Solution().subarraysDivByK([4,5,0,-2,-3,1], 5)
        7
        >>> Solution().subarraysDivByK([5], 9)
        0
        """
        n = len(nums)
        h = [None] * n
        h[0] = nums[0] % k
        for i in range(1, n):
            h[i] = h[i-1] + (nums[i] % k)
            h[i] %= k
        c = 0
        d = defaultdict()
        for k in h:
            if k in d.keys():
                c += d[k]
                d[k] = d[k] + 1
            else:
                d[k] = 1
                if k == 0:
                    c += 1
                    d[0] = 2
        return c


if __name__ == "__main__":
    import doctest

    doctest.testmod()
