from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        You are given an m x n integer matrix matrix with the following
        two properties:

        - Each row is sorted in non-decreasing order.
        - The first integer of each row is greater than the last integer of
        the previous row.

        Given an integer target, return true if target is in matrix
        or false otherwise.

        You must write a solution in O(log(m * n)) time complexity.

        >>> Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
        True
        >>> Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
        False
        """
        low = 0
        hight = len(matrix)-1
        while low <= hight:
            mid = (low + hight)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return target in matrix[mid]
            if matrix[mid][0] > target:
                hight = mid - 1
            if matrix[mid][-1] < target:
                low = mid + 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
