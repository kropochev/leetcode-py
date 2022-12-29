import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        You are given n tasks labeled from 0 to n - 1 represented by a 2D
        integer array tasks, where tasks[i] = [enqueueTime i, processingTime i]
        means that the ith task will be available to process at enqueueTime i
        and will take processingTime i to finish processing.

        You have a single-threaded CPU that can process at most one task at
        a time and will act in the following way:

        - If the CPU is idle and there are no available tasks to process,
        the CPU remains idle.
        - If the CPU is idle and there are available tasks, the CPU will choose
        the one with the shortest processing time. If multiple tasks have
        the same shortest processing time, it will choose the task with
        the smallest index.
        - Once a task is started, the CPU will process the entire task without
        stopping.
        - The CPU can finish a task then start a new one instantly.

        Return the order in which the CPU will process the tasks.

        >>> Solution().getOrder([[1,2],[2,4],[3,2],[4,1]])
        [0, 2, 3, 1]
        >>> Solution().getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]])
        [4, 3, 2, 0, 1]
        """
        htasks = []
        waiting = []
        result = []
        for i, (enqueueTime, processingTime) in enumerate(tasks):
            heapq.heappush(htasks, (enqueueTime, processingTime, i))

        while htasks or waiting:
            if waiting:
                processingTime, i = heapq.heappop(waiting)
            else:
                enqueueTime, processingTime, i = heapq.heappop(htasks)
                finishTime = enqueueTime
            finishTime += processingTime
            result += [i]
            while htasks and htasks[0][0] <= finishTime:
                enqueueTime, processingTime, i = heapq.heappop(htasks)
                heapq.heappush(waiting, (processingTime, i))

        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
