from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        It is a sweltering summer day, and a boy wants to buy some ice cream
        bars.
        At the store, there are n ice cream bars. You are given an array
        costs of length n, where costs[i] is the price of the ith ice cream bar
        in coins. The boy initially has coins coins to spend, and he wants
        to buy as many ice cream bars as possible.

        Return the maximum number of ice cream bars the boy can buy
        with coins coins.
        Note: The boy can buy the ice cream bars in any order.

        >>> Solution().maxIceCream([1,3,2,4,1], 7)
        4
        >>> Solution().maxIceCream([10,6,8,7,7,8], 5)
        0
        >>> Solution().maxIceCream([1,6,3,1,2,5], 20)
        6
        """
        if min(costs) > coins:
            return 0
        elif min(costs) == coins:
            return 1
        else:
            i = 0
            costs.sort()
            while coins >= 0 and costs:
                p = costs.pop(0)
                if p <= coins:
                    coins -= p
                    i += 1
                else:
                    break
            return i


if __name__ == "__main__":
    import doctest

    doctest.testmod()
