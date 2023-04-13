from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        Given two integer arrays pushed and popped each with distinct values,
        return true if this could have been the result of a sequence of push
        and pop operations on an initially empty stack, or false otherwise.

        >>> Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1])
        True
        >>> Solution().validateStackSequences([1,2,3,4,5], [4,3,5,1,2])
        False
        >>> Solution().validateStackSequences([1,0], [1,0])
        True
        """
        pop = 0
        stack = []
        for push in pushed:
            stack.append(push)
            while stack and stack[-1] == popped[pop]:
                stack.pop()
                pop += 1

        return not stack


if __name__ == "__main__":
    import doctest

    doctest.testmod()
