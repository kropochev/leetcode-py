from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        There are n kids with candies. You are given an integer array candies,
        where each candies[i] represents the number of candies the ith kid has,
        and an integer extraCandies, denoting the number of extra candies
        that you have.

        Return a boolean array result of length n, where result[i] is true if,
        after giving the ith kid all the extraCandies, they will have
        the greatest number of candies among all the kids, or false otherwise.

        Note that multiple kids can have the greatest number of candies.

        >>> Solution().kidsWithCandies([2,3,5,1,3], 3)
        [True, True, True, False, True]
        >>> Solution().kidsWithCandies([4,2,1,1,2], 1)
        [True, False, False, False, False]
        >>> Solution().kidsWithCandies([12,1,12], 10)
        [True, False, True]
        """
        return [candy + extraCandies >= max(candies) for candy in candies]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
