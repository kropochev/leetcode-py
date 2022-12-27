from typing import List


class Solution:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int
    ) -> int:
        """
        You have n bags numbered from 0 to n - 1. You are given two 0-indexed
        integer arrays capacity and rocks. The ith bag can hold a maximum
        of capacity[i] rocks and currently contains rocks[i] rocks.
        You are also given an integer additionalRocks, the number of additional
        rocks you can place in any of the bags.

        Return the maximum number of bags that could have full capacity after
        placing the additional rocks in some bags.

        >>> Solution().maximumBags([2,3,4,5], [1,2,4,4], 2)
        3
        >>> Solution().maximumBags([10,2,2], [2,2,0], 100)
        3
        """
        result = 0
        temp = []
        for c, r in zip(capacity, rocks):
            if c - r == 0:
                result += 1
            else:
                temp.append(c - r)

        for e in sorted(temp):
            if additionalRocks >= e:
                result += 1
                additionalRocks -= e
            else:
                break
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
