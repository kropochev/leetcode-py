from typing import List
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Given a string containing digits from 2-9 inclusive,
        return all possible letter combinations that the number could represent.
        Return the answer in any order.

        A mapping of digits to letters (just like on the telephone buttons)
        is given below. Note that 1 does not map to any letters.

        >>> Solution().letterCombinations("23")
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        >>> Solution().letterCombinations("")
        []
        >>> Solution().letterCombinations("2")
        ['a', 'b', 'c']
        """
        if not digits:
            return []

        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return [''.join(p) for p in product(*[m[d] for d in digits])]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
