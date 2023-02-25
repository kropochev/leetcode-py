from collections import defaultdict
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """
        A cinema has n rows of seats, numbered from 1 to n and there are ten
        seats in each row, labelled from 1 to 10 as shown in the figure above.

        Given the array reservedSeats containing the numbers of seats already
        reserved, for example, reservedSeats[i] = [3,8] means the seat located
        in row 3 and labelled with 8 is already reserved.

        Return the maximum number of four-person groups you can assign on
        the cinema seats. A four-person group occupies four adjacent seats
        in one single row. Seats across an aisle (such as [3,3] and [3,4])
        are not considered to be adjacent, but there is an exceptional case
        on which an aisle split a four-person group, in that case,
        the aisle split a four-person group in the middle, which means
        to have two people on each side.

        >>> Solution().maxNumberOfFamilies(3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]])
        4
        >>> Solution().maxNumberOfFamilies(2, [[2,1],[1,8],[2,6]])
        2
        >>> Solution().maxNumberOfFamilies(4, [[4,3],[1,4],[4,6],[1,7]])
        4
        """
        alloc1 = (60, 240, 960)
        alloc2 = 1020
        reserv = defaultdict(list)
        for row, seat in reservedSeats:
            reserv[row].append(seat)

        ans = 0
        for seats in reserv.values():
            row_reserv = 0
            for seat in seats:
                row_reserv |= 1 << seat
            if alloc2 & row_reserv == 0:
                ans += 2
                continue
            for alloc in alloc1:
                if alloc & row_reserv == 0:
                    ans += 1
                    break
        ans += (n - len(reserv)) * 2
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
