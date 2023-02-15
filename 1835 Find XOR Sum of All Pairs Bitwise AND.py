from typing import List
from operator import xor
from functools import reduce


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        """
        The XOR sum of a list is the bitwise XOR of all its elements.
        If the list only contains one element, then its XOR sum will be equal
        to this element.

        - For example, the XOR sum of [1,2,3,4] is equal to 1 XOR 2 XOR 3
        XOR 4 = 4, and the XOR sum of [3] is equal to 3.
        You are given two 0-indexed arrays arr1 and arr2 that consist only of
        non-negative integers.

        Consider the list containing the result of arr1[i] AND arr2[j]
        (bitwise AND) for every (i, j) pair where 0 <= i < arr1.length and
        0 <= j < arr2.length.

        Return the XOR sum of the aforementioned list.

        >>> Solution().getXORSum([1,2,3], [6,5])
        0
        >>> Solution().getXORSum([12], [4])
        4
        """

        return reduce(xor, arr1) & reduce(xor, arr2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
