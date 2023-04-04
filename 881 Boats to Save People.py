from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        You are given an array people where people[i] is the weight of the ith
        person, and an infinite number of boats where each boat can carry
        a maximum weight of limit. Each boat carries at most two people
        at the same time, provided the sum of the weight of those people
        is at most limit.

        Return the minimum number of boats to carry every given person.

        >>> Solution().numRescueBoats([1,2], 3)
        1
        >>> Solution().numRescueBoats([3,2,2,1], 3)
        3
        >>> Solution().numRescueBoats([3,5,3,4], 5)
        4
        >>> Solution().numRescueBoats([3,2,3,2,2], 6)
        3
        >>> Solution().numRescueBoats([2,4], 5)
        2
        """
        people.sort()
        ans = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if people[right] + people[left] <= limit:
                left += 1
            ans += 1
            right -= 1
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
