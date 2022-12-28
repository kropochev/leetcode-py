import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """
        You are given a 0-indexed integer array piles, where piles[i]
        represents the number of stones in the ith pile, and an integer k.
        You should apply the following operation exactly k times:

        - Choose any piles[i] and remove floor(piles[i] / 2) stones from it.

        Notice that you can apply the operation on the same pile more than once.

        Return the minimum possible total number of stones remaining after
        applying the k operations.

        floor(x) is the greatest integer that is smaller than
        or equal to x (i.e., rounds x down).

        >>> Solution().minStoneSum([5,4,9], 2)
        12
        >>> Solution().minStoneSum([4,3,6,7], 3)
        12
        """
        arr = [-pile for pile in piles]
        heapq.heapify(arr)

        for _ in range(k):
            heapq.heappush(arr, heapq.heappop(arr)//2)
        return -sum(arr)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
