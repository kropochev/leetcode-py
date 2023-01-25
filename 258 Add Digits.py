class Solution:
    def addDigits(self, num: int) -> int:
        """
        Given an integer num, repeatedly add all its digits until the result
        has only one digit, and return it.

        >>> Solution().addDigits(38)
        2
        >>> Solution().addDigits(0)
        0
        """
        def addition(num: int) -> int:
            ans = 0
            while num:
                ans += num % 10
                num = (num - num % 10)//10
                if ans > 9:
                    ans = addition(ans)
            return ans
        return addition(num)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
