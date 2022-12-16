class MyQueue:
    """
    Implement a first in first out (FIFO) queue using only two stacks.
    The implemented queue should support all the functions
    of a normal queue (push, peek, pop, and empty).

    Implement the MyQueue class:
    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.

    Notes:
    You must use only standard operations of a stack, which means only push
    to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, the stack may not be supported natively.
    You may simulate a stack using a list or deque (double-ended queue)
    as long as you use only a stack's standard operations.

    >>> myQueue = MyQueue()
    >>> myQueue.push(1)
    >>> myQueue.push(2)
    >>> myQueue.peek()
    1
    >>> myQueue.pop()
    1
    >>> myQueue.empty()
    False
    """

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._rearrange()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._rearrange()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _rearrange(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
