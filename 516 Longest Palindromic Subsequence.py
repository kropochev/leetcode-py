class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Given a string s, find the longest palindromic subsequence's
        length in s.

        A subsequence is a sequence that can be derived from another sequence
        by deleting some or no elements without changing the order of
        the remaining elements.

        >>> Solution().longestPalindromeSubseq('bbbab')
        4
        >>> Solution().longestPalindromeSubseq('cbbd')
        2
        """
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for k in range(2, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                if s[i] == s[j] and k == 2:
                    dp[i][j] = 2
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][n - 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
