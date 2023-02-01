from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        You are the manager of a basketball team. For the upcoming tournament,
        you want to choose the team with the highest overall score. The score
        of the team is the sum of scores of all the players in the team.

        However, the basketball team is not allowed to have conflicts.
        A conflict exists if a younger player has a strictly higher score
        than an older player. A conflict does not occur between players
        of the same age.

        Given two lists, scores and ages, where each scores[i] and ages[i]
        represents the score and age of the ith player, respectively,
        return the highest overall score of all possible basketball teams.

        >>> Solution().bestTeamScore([1,3,5,10,15], [1,2,3,4,5])
        34
        >>> Solution().bestTeamScore([4,5,6,5], [2,1,2,1])
        16
        >>> Solution().bestTeamScore([1,2,3,5], [8,9,10,1])
        6
        """
        store = sorted(zip(ages, scores))
        n = len(store)
        dp = [None] * n
        ans = 0
        for i in range(n):
            dp[i] = store[i][1]
            ans = max(ans, dp[i])
        for i in range(n):
            for j in range(i-1, -1, -1):
                if store[i][1] >= store[j][1]:
                    dp[i] = max(dp[i], dp[j]+store[i][1])
            ans = max(ans, dp[i])
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
