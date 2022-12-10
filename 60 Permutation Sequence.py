from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

        By listing and labeling all of the permutations in order,
        we get the following sequence for n = 3:
        "123"
        "132"
        "213"
        "231"
        "312"
        "321"
        Given n and k, return the k^th permutation sequence.

        >>> Solution().getPermutation(3, 3)
        '213'
        >>> Solution().getPermutation(4, 9)
        '2314'
        >>> Solution().getPermutation(3, 1)
        '123'
        """
        for i, seq in enumerate(
            permutations([str(n) for n in range(1, n + 1)]), start=1
        ):
            if k == i:
                return "".join(seq)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
