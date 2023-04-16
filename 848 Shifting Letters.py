from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        """
        You are given a string s of lowercase English letters and an integer
        array shifts of the same length.

        Call the shift() of a letter, the next letter in the alphabet,
        (wrapping around so that 'z' becomes 'a').

        For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
        Now for each shifts[i] = x, we want to shift the first i + 1 letters
        of s, x times.

        Return the final string after all such shifts to s are applied.

        >>> Solution().shiftingLetters("abc", [3,5,9])
        'rpl'
        >>> Solution().shiftingLetters("aaa", [1,2,3])
        'gfd'
        """
        def shift(c: str, k: int) -> str:
            k -= k // 26 * 26
            if ord(c) - ord('a') + k >= 26:
                k -= 26
            return chr(ord(c) + k)

        total, s = sum(shifts), list(s)
        for i in range(len(shifts)):
            total, s[i] = total - shifts[i], shift(s[i], total)
        return ''.join(s)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
