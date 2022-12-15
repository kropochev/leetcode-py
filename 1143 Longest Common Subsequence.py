class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Given two strings text1 and text2, return the length of their longest
        common subsequence. If there is no common subsequence, return 0.

        A subsequence of a string is a new string generated from the original
        string with some characters (can be none) deleted without changing
        the relative order of the remaining characters.

        For example, "ace" is a subsequence of "abcde".

        A common subsequence of two strings is a subsequence that is common
        to both strings.

        >>> Solution().longestCommonSubsequence("abcde", "ace")
        3
        >>> Solution().longestCommonSubsequence("abc", "abc")
        3
        >>> Solution().longestCommonSubsequence("abc", "def")
        0
        """
        m = len(text1)+1
        n = len(text2)+1
        dp = [[0] * (n) for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
