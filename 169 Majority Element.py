from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Given an array nums of size n, return the majority element.
        The majority element is the element that appears more than ⌊n / 2⌋
        times. You may assume that the majority element always exists in the
        array.

        >>> Solution().majorityElement([3,2,3])
        3
        >>> Solution().majorityElement([2,2,1,1,1,2,2])
        2
        """
        d = {}
        for n in nums:
            if n not in d.keys():
                d[n] = 1
            else:
                d[n] += 1
        return max(d, key=d.get)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
