class Solution:
    def minInsertions(self, s: str) -> int:
        """
        Given a string s. In one step you can insert any character at any index
        of the string.

        Return the minimum number of steps to make s palindrome.

        A Palindrome String is one that reads the same backward as well as
        forward.

        >>> Solution().minInsertions("zzazz")
        0
        >>> Solution().minInsertions("mbadm")
        2
        >>> Solution().minInsertions("leetcode")
        5
        """
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in reversed(range(n)):
            for j in range(i, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
