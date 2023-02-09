from typing import List
from collections import defaultdict


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        """
        You are given an array of strings ideas that represents a list of names
        to be used in the process of naming a company. The process of naming
        a company is as follows:

        Choose 2 distinct names from ideas, call them ideaA and ideaB.
        Swap the first letters of ideaA and ideaB with each other.
        If both of the new names are not found in the original ideas,
        then the name ideaA ideaB (the concatenation of ideaA and ideaB,
        separated by a space) is a valid company name.
        Otherwise, it is not a valid name.

        Return the number of distinct valid names for the company.

        >>> Solution().distinctNames(["coffee","donuts","time","toffee"])
        6
        >>> Solution().distinctNames(["lack","back"])
        0
        """

        d = defaultdict(set)
        for idea in ideas:
            d[idea[0]].add(idea[1:])

        arr = list(d.keys())
        ans, n = 0, len(arr)
        for i in range(len(arr)):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]
                ans += len(d[a] - d[b]) * len(d[b] - d[a]) * 2
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
