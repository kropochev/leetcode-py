class Solution:
    def removeStars(self, s: str) -> str:
        """
        You are given a string s, which contains stars *.

        In one operation, you can:
        - Choose a star in s.
        - Remove the closest non-star character to its left, as well as remove
        the star itself.
        - Return the string after all stars have been removed.

        Note:
        - The input will be generated such that the operation is always
        possible.
        - It can be shown that the resulting string will always be unique.

        >>> Solution().removeStars('leet**cod*e')
        'lecoe'
        >>> Solution().removeStars('erase*****')
        ''
        """
        ans = ''
        star = 0
        for c in s[::-1]:
            if c == '*':
                star += 1
            elif c != '*' and star:
                star -= 1
            else:
                ans += c
        return ans[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
