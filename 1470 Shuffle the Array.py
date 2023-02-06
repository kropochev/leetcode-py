from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Given the array nums consisting of 2n elements
        in the form [x1,x2,...,xn,y1,y2,...,yn].

        Return the array in the form [x1,y1,x2,y2,...,xn,yn].

        >>> Solution().shuffle([2,5,1,3,4,7], 3)
        [2, 3, 5, 4, 1, 7]
        >>> Solution().shuffle([1,1,2,2], 2)
        [1, 2, 1, 2]
        >>> Solution().shuffle([1,2,3,4,4,3,2,1], 4)
        [1, 4, 2, 3, 3, 2, 4, 1]
        """ 
        ans = []
        for i, j in zip(nums[:n], nums[n:]):
            ans += [i, j]
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
