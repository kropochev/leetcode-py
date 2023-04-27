class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        There are n bulbs that are initially off. You first turn on all
        the bulbs, then you turn off every second bulb.

        On the third round, you toggle every third bulb (turning on if it's off
        or turning off if it's on). For the ith round, you toggle every i bulb.
        For the nth round, you only toggle the last bulb.

        Return the number of bulbs that are on after n rounds.

        >>> Solution().bulbSwitch(3)
        1
        >>> Solution().bulbSwitch(0)
        0
        >>> Solution().bulbSwitch(1)
        1
        """
        i, s = 0, 3
        while n > 0:
            n -= s
            s += 2
            i += 1
        return i


if __name__ == "__main__":
    import doctest

    doctest.testmod()
