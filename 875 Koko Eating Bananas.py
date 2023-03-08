from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Koko loves to eat bananas. There are n piles of bananas,
        the ith pile has piles[i] bananas. The guards have gone
        and will come back in h hours.

        Koko can decide her bananas-per-hour eating speed of k. Each hour,
        she chooses some pile of bananas and eats k bananas from that pile.
        If the pile has less than k bananas, she eats all of them instead
        and will not eat any more bananas during this hour.

        Koko likes to eat slowly but still wants to finish eating all
        the bananas before the guards return.

        Return the minimum integer k such that she can eat all the bananas
        within h hours.

        >>> Solution().minEatingSpeed([3,6,7,11], 8)
        4
        >>> Solution().minEatingSpeed([30,11,23,4,20], 5)
        30
        >>> Solution().minEatingSpeed([30,11,23,4,20], 6)
        23
        """
        left = (sum(piles) + h-1) // h
        right = max(piles) + 1
        while left < right:
            k = (left + right) // 2
            t = sum((p + k - 1) // k for p in piles)
            if t <= h:
                right = k
            else:
                left = k + 1
        return left


if __name__ == "__main__":
    import doctest

    doctest.testmod()
