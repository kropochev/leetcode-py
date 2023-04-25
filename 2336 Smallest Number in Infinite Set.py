import heapq


class SmallestInfiniteSet:
    """
    You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

    Implement the SmallestInfiniteSet class:
    - SmallestInfiniteSet() Initializes the SmallestInfiniteSet object
    to contain all positive integers.
    - int popSmallest() Removes and returns the smallest integer contained
    in the infinite set.
    - void addBack(int num) Adds a positive integer num back into the infinite
    set, if it is not already in the infinite set.

    >>> obj = SmallestInfiniteSet()
    >>> obj.addBack(2)
    >>> obj.popSmallest()
    1
    >>> obj.popSmallest()
    2
    >>> obj.popSmallest()
    3
    >>> obj.addBack(1)
    >>> obj.popSmallest()
    1
    >>> obj.popSmallest()
    4
    >>> obj.popSmallest()
    5
    """

    def __init__(self):
        self.s = [i for i in range(1, 1001)]
        heapq.heapify(self.s)

    def popSmallest(self) -> int:
        if self.s:
            return heapq.heappop(self.s)

    def addBack(self, num: int) -> None:
        if num not in self.s:
            heapq.heappush(self.s, num)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
