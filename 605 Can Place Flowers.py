from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        You have a long flowerbed in which some of the plots are planted,
        and some are not. However, flowers cannot be planted in adjacent plots.

        Given an integer array flowerbed containing 0's and 1's, where 0 means
        empty and 1 means not empty, and an integer n, return if n new flowers
        can be planted in the flowerbed without violating
        the no-adjacent-flowers rule.

        >>> Solution().canPlaceFlowers([1,0,0,0,1], 1)
        True
        >>> Solution().canPlaceFlowers([1,0,0,0,1], 2)
        False
        """
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        count = 2 if flowerbed[0] == 0 else 0
        prev = flowerbed[0]
        for i in range(1, len(flowerbed)):
            if i == len(flowerbed)-1 and flowerbed[i] == 0:
                count += 1
            if prev == 0 and flowerbed[i] == 0:
                count += 1
            elif prev == 0 and flowerbed[i] == 1:
                n -= (count-1)//2
                count = 0
            elif prev == 1 and flowerbed[i] == 0:
                count += 1
            prev = flowerbed[i]
        if count:
            n -= (count-1)//2
        return n <= 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
