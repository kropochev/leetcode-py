from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        A chef has collected data on the satisfaction level of his n dishes.
        Chef can cook any dish in 1 unit of time.

        Like-time coefficient of a dish is defined as the time taken to cook
        that dish including previous dishes multiplied by its satisfaction
        level i.e. time[i] * satisfaction[i].

        Return the maximum sum of like-time coefficient that the chef
        can obtain after dishes preparation.

        Dishes can be prepared in any order and the chef can discard some
        dishes to get this maximum value.

        >>> Solution().maxSatisfaction([-1,-8,0,5,-9])
        14
        >>> Solution().maxSatisfaction([4,3,2])
        20
        >>> Solution().maxSatisfaction([-1,-4,-5])
        0
        """
        ans = 0
        satisfaction.sort(reverse=True)
        length = len(satisfaction)
        while length > 1:
            tmp, n = 0, length
            for s in satisfaction:
                tmp += s * n
                n -= 1
                if n == 0:
                    break
            if tmp > ans:
                ans = tmp
            length -= 1
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
