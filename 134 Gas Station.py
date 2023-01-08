from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        There are n gas stations along a circular route, where the amount
        of gas at the ith station is gas[i].

        You have a car with an unlimited gas tank and it costs cost[i] of gas
        to travel from the ith station to its next (i + 1)th station.
        You begin the journey with an empty tank at one of the gas stations.

        Given two integer arrays gas and cost, return the starting gas
        station's index if you can travel around the circuit
        once in the clockwise direction, otherwise return -1. If there exists
        a solution, it is guaranteed to be unique

        >>> Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
        3
        >>> Solution().canCompleteCircuit([2,3,4], [3,4,3])
        -1
        """
        if sum(cost) > sum(gas):
            return -1
        start, tank = 0, 0
        for i in range(0, len(gas)-1):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start


if __name__ == "__main__":
    import doctest

    doctest.testmod()
