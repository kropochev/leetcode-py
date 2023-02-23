import heapq
from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        """
        Suppose LeetCode will start its IPO soon. In order to sell a good price
        of its shares to Venture Capital, LeetCode would like to work on some
        projects to increase its capital before the IPO. Since it has limited
        resources, it can only finish at most k distinct projects before
        the IPO. Help LeetCode design the best way to maximize its total
        capital after finishing at most k distinct projects.

        You are given n projects where the ith project has a pure profit
        profits[i] and a minimum capital of capital[i] is needed to start it.

        Initially, you have w capital. When you finish a project,
        you will obtain its pure profit and the profit will be added
        to your total capital.

        Pick a list of at most k distinct projects from given projects
        to maximize your final capital, and return the final maximized capital.

        >>> Solution().findMaximizedCapital(2, 0, [1,2,3], [0,1,1])
        4
        >>> Solution().findMaximizedCapital(3, 0, [1,2,3], [0,1,2])
        6
        """
        projects = [(c, p) for c, p in zip(capital, profits)]
        projects.sort()

        available_projects = []
        i = 0

        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(available_projects, -projects[i][1])
                i += 1
            if not available_projects:
                break
            w -= heapq.heappop(available_projects)
        return w


if __name__ == "__main__":
    import doctest

    doctest.testmod()
