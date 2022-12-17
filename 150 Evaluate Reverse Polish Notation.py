from typing import List
from operator import add, sub, mul, truediv


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate the value of an arithmetic expression
        in Reverse Polish Notation.

        Valid operators are +, -, *, and /. Each operand may be an integer
        or another expression.

        Note that division between two integers should truncate toward zero.

        It is guaranteed that the given RPN expression is always valid.
        That means the expression would always evaluate to a result,
        and there will not be any division by zero operation.

        >>> Solution().evalRPN(["2","1","+","3","*"])
        9
        >>> Solution().evalRPN(["4","13","5","/","+"])
        6
        >>> Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
        22
        """
        operators = {'+': add, '-': sub, '*': mul, '/': truediv}

        stack = []
        while tokens:
            token = tokens.pop(0)
            if token in operators:
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(int(operators[token](val1, val2)))
            else:
                stack.append(int(token))

        return stack.pop()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
