from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        """
        Given two integer arrays arr1 and arr2, and the integer d,
        return the distance value between the two arrays.

        The distance value is defined as the number of elements arr1[i]
        such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

        >>> Solution().findTheDistanceValue([4,5,8], [10,9,1,8], 2)
        2
        >>> Solution().findTheDistanceValue([1,4,2,3], [-4,-3,6,10,20,30], 3)
        2
        >>> Solution().findTheDistanceValue([2,1,100,3], [-5,-2,10,-3,7], 6)
        1
        """
        return sum(all([abs(v1-v2) > d for v2 in arr2]) for v1 in arr1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
