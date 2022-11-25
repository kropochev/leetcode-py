class Solution:
    def minPartitions(self, n: str) -> int:
        """
        A decimal number is called deci-binary if each of its digits
        is either 0 or 1 without any leading zeros. For example,
        101 and 1100 are deci-binary, while 112 and 3001 are not.

        Given a string n that represents a positive decimal integer,
        return the minimum number of positive deci-binary numbers needed
        so that they sum up to n.

        >>> Solution().minPartitions("32")
        3
        >>> Solution().minPartitions("82734")
        8
        >>> Solution().minPartitions("27346209830709182346")
        9
        """

        for i in range(9, 0, -1):
            if str(i) in n:
                return i


if __name__ == "__main__":
    import doctest

    doctest.testmod()
