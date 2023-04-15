from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        """
        There are n piles of coins on a table. Each pile consists of a positive
        number of coins of assorted denominations.

        In one move, you can choose any coin on top of any pile, remove it,
        and add it to your wallet.

        Given a list piles, where piles[i] is a list of integers denoting
        the composition of the ith pile from top to bottom, and a positive
        integer k, return the maximum total value of coins you can have in your
        wallet if you choose exactly k coins optimally.

        >>> Solution().maxValueOfCoins([[1,100,3],[7,8,9]], 2)
        101
        >>> Solution().maxValueOfCoins([[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], 7)
        706
        """
        n = len(piles)
        dp = [[-1] * (k + 1) for _ in range(n + 1)]

        def f(i: int, coins: int) -> int:
            if i == 0:
                return 0
            if dp[i][coins] != -1:
                return dp[i][coins]
            curr_sum = 0
            for curr_coins in range(min(len(piles[i - 1]), coins) + 1):
                if curr_coins > 0:
                    curr_sum += piles[i - 1][curr_coins - 1]
                dp[i][coins] = max(
                    dp[i][coins], f(i - 1, coins - curr_coins) + curr_sum
                )

            return dp[i][coins]

        return f(n, k)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
