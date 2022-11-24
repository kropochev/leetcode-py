class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        You are playing the Bulls and Cows game with your friend.

        You write down a secret number and ask your friend to guess what
        the number is. When your friend makes a guess, you provide a hint with
        the following info:

        - The number of "bulls", which are digits in the guess that
        are in the correct position.
        - The number of "cows", which are digits in the guess that are in your
        secret number but are located in the wrong position. Specifically,
        the non-bull digits in the guess that could be rearranged such that
        they become bulls.

        Given the secret number secret and your friend's guess guess,
        return the hint for your friend's guess.

        The hint should be formatted as "xAyB", where x is the number of bulls
        and y is the number of cows. Note that both secret and guess
        may contain duplicate digits.

        >>> Solution().getHint("1807", "7810")
        '1A3B'
        >>> Solution().getHint("1123", "0111")
        '1A1B'
        """
        from collections import Counter

        counter_guess = Counter(guess)

        b, c = 0, 0
        e = []

        for i, d in enumerate(secret):
            if d == guess[i]:
                b += 1
                counter_guess[d] -= 1
            else:
                e.append(d)

        for d in e:
            if counter_guess[d] > 0:
                c += 1
                counter_guess[d] -= 1

        return "{}A{}B".format(b, c)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
