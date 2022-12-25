from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        You are given an integer array nums of length n, and an integer array
        queries of length m.

        Return an array answer of length m where answer[i] is the maximum
        size of a subsequence that you can take from nums such that
        the sum of its elements is less than or equal to queries[i].

        A subsequence is an array that can be derived from another array
        by deleting some or no elements without changing the order
        of the remaining elements.

        >>> Solution().answerQueries([4,5,2,1], [3,10,21])
        [2, 3, 4]
        >>> Solution().answerQueries([2,3,4,5], [1])
        [0]
        """
        nums.sort()
        result = []
        n = len(nums)
        for i in queries:
            s, j = 0, 0
            while j < n and s <= i:
                s += nums[j]
                j += 1
            if j == n and s <= i:
                result.append(j)
            else:
                result.append(j-1)
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
