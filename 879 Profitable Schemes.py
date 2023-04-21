from typing import List


class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profits: List[int]
    ) -> int:
        """
        There is a group of n members, and a list of various crimes they could
        commit. The ith crime generates a profit[i] and requires group[i]
        members to participate in it. If a member participates in one crime,
        that member can't participate in another crime.

        Let's call a profitable scheme any subset of these crimes
        that generates at least minProfit profit, and the total number
        of members participating in that subset of crimes is at most n.

        Return the number of schemes that can be chosen. Since the answer
        may be very large, return it modulo 10^9 + 7.

        >>> Solution().profitableSchemes(5, 3, [2,2], [2,3])
        2
        >>> Solution().profitableSchemes(10, 5, [2,3,5], [6,7,8])
        7
        """
        dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
        for count in range(n + 1):
            dp[len(group)][count][minProfit] = 1
        for index in range(len(group) - 1, -1, -1):
            for count in range(n + 1):
                for profit in range(minProfit + 1):
                    dp[index][count][profit] = dp[index + 1][count][profit]
                    if count + group[index] <= n:
                        dp[index][count][profit] = (
                            dp[index][count][profit]
                            + dp[index + 1][count + group[index]][
                                min(minProfit, profit + profits[index])
                            ]
                        ) % 1000000007

        return dp[0][0][0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
