from typing import List
from operator import xor
from functools import reduce
from itertools import combinations


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        The XOR total of an array is defined as the bitwise XOR
        of all its elements, or 0 if the array is empty.

        For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
        Given an array nums, return the sum of all XOR totals for every subset
        of nums.

        Note: Subsets with the same elements should be counted multiple times.

        An array a is a subset of an array b if a can be obtained from b
        by deleting some (possibly zero) elements of b.

        >>> Solution().subsetXORSum([1,3])
        6
        >>> Solution().subsetXORSum([5,1,6])
        28
        >>> Solution().subsetXORSum([3,4,5,6,7,8])
        480
        """
        res = 0
        for i in range(1, len(nums) + 1):
            for e in combinations(nums, i):
                res += reduce(xor, e)
        return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
