class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Given two strings word1 and word2, return the minimum number
        of operations required to convert word1 to word2.

        You have the following three operations permitted on a word:
        - Insert a character
        - Delete a character
        - Replace a character

        >>> Solution().minDistance("horse", "ros")
        3
        >>> Solution().minDistance("intention", "execution")
        5
        """
        d = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        d[0] = [*range(len(word2) + 1)]
        for n, row in enumerate(d):
            row[0] = n

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1])
                else:
                    d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + 1)
        return d[-1][-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
