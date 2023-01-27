from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        Given an integer n, return a string array answer (1-indexed) where:
        - answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
        - answer[i] == "Fizz" if i is divisible by 3.
        - answer[i] == "Buzz" if i is divisible by 5.
        - answer[i] == i (as a string) if none of the above conditions are true.

        >>> Solution().fizzBuzz(3)
        ['1', '2', 'Fizz']
        >>> Solution().fizzBuzz(5)
        ['1', '2', 'Fizz', '4', 'Buzz']
        >>> Solution().fizzBuzz(15)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        """
        ans = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append('FizzBuzz')
            elif i % 3 == 0:
                ans.append('Fizz')
            elif i % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(i))
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
