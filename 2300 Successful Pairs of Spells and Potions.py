from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        """
        You are given two positive integer arrays spells and potions, of length
        n and m respectively, where spells[i] represents the strength of
        the ith spell and potions[j] represents the strength of the jth potion.

        You are also given an integer success. A spell and potion pair is
        considered successful if the product of their strengths is at least
        success.

        Return an integer array pairs of length n where pairs[i] is the number
        of potions that will form a successful pair with the ith spell.

        >>> Solution().successfulPairs([5,1,3], [1,2,3,4,5], 7)
        [4, 0, 3]
        >>> Solution().successfulPairs([3,1,2], [8,5,8], 16)
        [2, 0, 2]
        """
        potions.sort()
        ans = [0] * len(spells)
        len_potions = len(potions)

        for i, spell in enumerate(spells):
            if spell * potions[-1] < success:
                ans[i] = 0
                continue
            left, right = 0, len_potions-1
            while left < right:
                mid = (left + right) // 2
                if potions[mid] * spell >= success:
                    right = mid
                else:
                    left = mid + 1
            ans[i] = len_potions - right
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
