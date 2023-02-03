class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given
        number of rows like this: (you may want to display this pattern in
        a fixed font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R

        And then read line by line: "PAHNAPLSIIGYIR"

        Write the code that will take a string and make this conversion given
        a number of rows.

        >>> Solution().convert("PAYPALISHIRING", 3)
        'PAHNAPLSIIGYIR'
        >>> Solution().convert("PAYPALISHIRING", 4)
        'PINALSIGYAHRPI'
        >>> Solution().convert("A", 1)
        'A'
        """
        m = [[] for _ in range(numRows)]
        i, c = 0, 0

        while i <= len(s)-1:
            if c % 2 == 0:
                for r in range(numRows):
                    m[r].append(s[i])
                    i += 1
                    if i == len(s):
                        break
            else:
                for r in range(numRows-2, 0, -1):
                    m[r].append(s[i])
                    i += 1
                    if i == len(s):
                        break
            c += 1

        return ''.join([i for r in m for i in r])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
