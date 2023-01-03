from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        You are given an array of n strings strs, all of the same length.
        The strings can be arranged such that there is one on each line,
        making a grid. For example, strs = ["abc", "bce", "cae"] can be
        arranged as:
            abc
            bce
            cae
        You want to delete the columns that are not sorted lexicographically.
        In the above example (0-indexed), columns 0 ('a', 'b', 'c')
        and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not,
        so you would delete column 1.

        Return the number of columns that you will delete.

        >>> Solution().minDeletionSize(["cba","daf","ghi"])
        1
        >>> Solution().minDeletionSize(["a","b"])
        0
        >>> Solution().minDeletionSize(["zyx","wvu","tsr"])
        3
        """
        res = 0
        for i in range(len(strs[0])):
            tmp = []
            _ = [tmp.append(n[i]) for n in strs]
            if tmp != sorted(tmp):
                res += 1
        return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
