class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        """
        A program was supposed to print an array of integers. The program
        forgot to print whitespaces and the array is printed as a string
        of digits s and all we know is that all integers in the array were
        in the range [1, k] and there are no leading zeros in the array.

        Given the string s and the integer k, return the number of the possible
        arrays that can be printed as s using the mentioned program.
        Since the answer may be very large, return it modulo 10^9 + 7.

        >>> Solution().numberOfArrays("1000", 10000)
        1
        >>> Solution().numberOfArrays("1000", 10)
        0
        >>> Solution().numberOfArrays("1317", 2000)
        8
        """
        dp = [0] * (len(s) + 1)

        def dfs(start: int) -> int:
            if dp[start]:
                return dp[start]
            if start == len(s):
                return 1
            if s[start] == '0':
                return 0
            count = 0
            for end in range(start, len(s)):
                if int(s[start:end+1]) > k:
                    break
                count += dfs(end + 1)
            dp[start] = count % 1000000007
            return count % 1000000007

        return dfs(0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
