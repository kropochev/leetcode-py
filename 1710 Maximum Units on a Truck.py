from typing import List
from operator import itemgetter


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        You are assigned to put some amount of boxes onto one truck.
        You are given a 2D array boxTypes,
        where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

        - numberOfBoxesi is the number of boxes of type i.
        - numberOfUnitsPerBoxi is the number of units in each box of the type i.

        You are also given an integer truckSize, which is the maximum number
        of boxes that can be put on the truck. You can choose any boxes to put
        on the truck as long as the number of boxes does not exceed truckSize.

        Return the maximum total number of units that can be put on the truck.

        >>> Solution().maximumUnits([[1,3],[2,2],[3,1]], 4)
        8
        >>> Solution().maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10)
        91
        """
        boxTypes.sort(key=itemgetter(1), reverse=True)
        res = 0
        for e in boxTypes:
            if truckSize >= e[0]:
                res += e[0]*e[1]
                truckSize -= e[0]
            else:
                res += truckSize*e[1]
                break
        return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
