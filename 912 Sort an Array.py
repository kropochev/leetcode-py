from typing import List


class Solution:
    def sortArray(self,  nums: List[int]) -> List[int]:
        """
        Given an array of integers nums,  sort the array in ascending order and
        return it.

        You must solve the problem without using any built-in functions
        in O(nlog(n)) time complexity and with the smallest space complexity
        possible.

        >>> Solution().sortArray([5, 2, 3, 1])
        [1, 2, 3, 5]
        >>> Solution().sortArray([5, 1, 1, 2, 0, 0])
        [0, 0, 1, 1, 2, 5]
        """

        if len(nums) < 2:
            return nums

        mid = len(nums) // 2
        left_arr = nums[:mid]
        right_arr = nums[mid:]
        self.sortArray(left_arr)
        self.sortArray(right_arr)
        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                nums[k] = left_arr[i]
                i += 1
            else:
                nums[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            nums[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            nums[k] = right_arr[j]
            j += 1
            k += 1

        return nums


if __name__ == "__main__":
    import doctest

    doctest.testmod()
