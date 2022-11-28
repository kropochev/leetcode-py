from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """
        You are given an integer array matches where
        matches[i] = [winneri, loseri] indicates that the player winneri
        defeated player loseri in a match.

        Return a list answer of size 2 where:
        - answer[0] is a list of all players that have not lost any matches.
        - answer[1] is a list of all players that have lost exactly one match.

        The values in the two lists should be returned in increasing order.

        Note:
        You should only consider the players that have played at least
        one match.
        The testcases will be generated such that no two matches will have
        the same outcome.

        >>> Solution().findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])
        [[1, 2, 10], [4, 5, 7, 8]]
        >>> Solution().findWinners([[2,3],[1,3],[5,4],[6,4]])
        [[1, 2, 5, 6], []]
        """
        from collections import Counter

        win = set()
        los = Counter()
        for m in matches:
            win.add(m[0])
            los[m[1]] += 1

        return [
            sorted(list(win.difference(los))),
            sorted([k for k, v in los.items() if v == 1]),
        ]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
