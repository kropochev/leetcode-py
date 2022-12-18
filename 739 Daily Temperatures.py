from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Given an array of integers temperatures represents the daily
        temperatures, return an array answer such that answer[i] is the number
        of days you have to wait after the ith day to get a warmer temperature.
        If there is no future day for which this is possible,
        keep answer[i] == 0 instead.

        >>> Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
        [1, 1, 4, 2, 1, 1, 0, 0]
        >>> Solution().dailyTemperatures([30,40,50,60])
        [1, 1, 1, 0]
        >>> Solution().dailyTemperatures([30,60,90])
        [1, 1, 0]
        """
        stack = [0]
        length = len(temperatures)
        answer = [0] * length

        for i in range(1, length):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
