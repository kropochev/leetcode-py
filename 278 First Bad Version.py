# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """You are a product manager and currently leading a team to develop
        a new product. Unfortunately, the latest version of your product fails
        the quality check. Since each version is developed based
        on the previous version, all the versions after a bad version
        are also bad.

        Suppose you have n versions [1, 2, ..., n] and you want to find out
        the first bad one, which causes all the following ones to be bad.

        You are given an API bool isBadVersion(version) which returns whether
        version is bad. Implement a function to find the first bad version.
        You should minimize the number of calls to the API.

        >>> Solution().firstBadVersion(5)
        4
        >>> Solution().firstBadVersion(1)
        1
        >>> Solution().firstBadVersion(3)
        1
        """

        if n == 1:
            return 1

        left = 1
        right = n
        while left < right:
            mid = (left+right)//2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    import doctest

    doctest.testmod()
