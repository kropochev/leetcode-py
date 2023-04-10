class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}',
        '[' and ']', determine if the input string is valid.

        An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.

        >>> Solution().isValid("()")
        True
        >>> Solution().isValid("()[]{}")
        True
        >>> Solution().isValid("(]")
        False
        >>> Solution().isValid("([)]")
        False
        >>> Solution().isValid("(){}}{")
        False
        >>> Solution().isValid("[([]])")
        False
        >>> Solution().isValid("{[]}")
        True
        >>> Solution().isValid("(([]){})")
        True
        >>> Solution().isValid("{}([{}{}][])[{}]")
        True
        >>> Solution().isValid("]")
        False
        >>> Solution().isValid("({{{{}}}))")
        False
        """

        stack = []
        for b in s:
            if b in ("(", "[", "{"):
                stack.append(b)
            if b in (")", "]", "}") and not stack:
                return False
            if b == ")" and "(" == stack.pop():
                continue
            elif b == "]" and "[" == stack.pop():
                continue
            elif b == "}" and "{" == stack.pop():
                continue
            elif b in (")", "]", "}"):
                return False

        return False if stack else True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
