from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given
        stock on the ith day.

        Find the maximum profit you can achieve. You may complete as many
        transactions as you like (i.e., buy one and sell one share of the stock
        multiple times) with the following restrictions:

        After you sell your stock, you cannot buy stock on the next day
        (i.e., cooldown one day).

        Note: You may not engage in multiple transactions simultaneously
        (i.e., you must sell the stock before you buy again).

        >>> Solution().maxProfit([1,2,3,0,2])
        3
        >>> Solution().maxProfit([1])
        0
        """

        length = len(prices)
        if length <= 1:
            return 0
        hold = [0]*(length+1)
        sold = [0]*(length+1)
        rest = [0]*(length+1)
        hold[1] = -prices[0]
        for i in range(2, length+1):
            hold[i] = max(hold[i-1], rest[i-1] - prices[i-1])
            sold[i] = hold[i-1] + prices[i-1]
            rest[i] = max(rest[i-1], sold[i-1])
        return max(rest[-1], sold[-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
