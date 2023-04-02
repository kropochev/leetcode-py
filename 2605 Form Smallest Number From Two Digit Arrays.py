from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Given two arrays of unique digits nums1 and nums2, return the smallest
        number that contains at least one digit from each array.

        >>> Solution().minNumber([4,1,3], [5,7])
        15
        >>> Solution().minNumber([3,5,2,6], [3,1,7])
        3
        """
        num = set(nums1).intersection(set(nums2))
        if num:
            return min(num)
        return min(min(nums1) * 10 + min(nums2), min(nums2) * 10 + min(nums1))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
