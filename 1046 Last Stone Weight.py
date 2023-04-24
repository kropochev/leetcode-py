import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        You are given an array of integers stones where stones[i] is the weight
        of the ith stone.

        We are playing a game with the stones. On each turn, we choose
        the heaviest two stones and smash them together. Suppose the heaviest
        two stones have weights x and y with x <= y.
        The result of this smash is:

        - If x == y, both stones are destroyed, and
        - If x != y, the stone of weight x is destroyed,
        and the stone of weight y has new weight y - x.

        At the end of the game, there is at most one stone left.

        Return the weight of the last remaining stone.
        If there are no stones left, return 0.

        >>> Solution().lastStoneWeight([2,7,4,1,8,1])
        1
        >>> Solution().lastStoneWeight([1])
        1
        >>> Solution().lastStoneWeight([10,10,4,4])
        0
        """
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            val1 = heapq.heappop(stones)
            val2 = heapq.heappop(stones)
            if val1 != val2:
                heapq.heappush(stones, val1 - val2)
        return -heapq.heappop(stones) if stones else 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
