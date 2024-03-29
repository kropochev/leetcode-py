from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Given an array of characters chars, compress it using the following
        algorithm:

        Begin with an empty string s. For each group of consecutive repeating
        characters in chars:
        - If the group's length is 1, append the character to s.
        - Otherwise, append the character followed by the group's length.

        The compressed string s should not be returned separately, but instead,
        be stored in the input character array chars. Note that group lengths
        that are 10 or longer will be split into multiple characters in chars.

        After you are done modifying the input array,
        return the new length of the array.

        You must write an algorithm that uses only constant extra space.

        >>> Solution().compress(['a','a','b','b','c','c','c'])
        6
        >>> Solution().compress(['a'])
        1
        >>> Solution().compress(['a','b','b','b','b','b','b','b','b','b','b','b','b'])
        4
        """
        if len(chars) == 1:
            return 1
        count = 1
        left, right = 1, len(chars) - 1
        while left <= right:
            if chars[left] != chars[left-1]:
                if count > 1:
                    for char in str(count):
                        chars.insert(left, char)
                        right += 1
                        left += 1
                left += 1
                count = 1
            else:
                chars.pop(left)
                right -= 1
                count += 1
        if count > 1:
            chars.extend([char for char in str(count)])
        return len(chars)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
