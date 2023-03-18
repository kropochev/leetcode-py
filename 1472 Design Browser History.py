class BrowserHistory:
    """
    You have a browser of one tab where you start on the homepage and
    you can visit another url, get back in the history number of steps or move
    forward in the history number of steps.

    Implement the BrowserHistory class:
    - BrowserHistory(string homepage) Initializes the object with the homepage
    of the browser.
    - void visit(string url) Visits url from the current page. It clears up all
    the forward history.
    - string back(int steps) Move steps back in history. If you can only return
    x steps in the history and steps > x, you will return only x steps.
    Return the current url after moving back in history at most steps.
    - string forward(int steps) Move steps forward in history. If you can only
    forward x steps in the history and steps > x, you will forward only x steps.
    Return the current url after forwarding in history at most steps.

    >>> browserHistory = BrowserHistory("leetcode.com")
    >>> browserHistory.visit("google.com")
    >>> browserHistory.visit("facebook.com")
    >>> browserHistory.visit("youtube.com")
    >>> browserHistory.back(1)
    'facebook.com'
    >>> browserHistory.back(1)
    'google.com'
    >>> browserHistory.forward(1)
    'facebook.com'
    >>> browserHistory.visit("linkedin.com")
    >>> browserHistory.forward(2)
    'linkedin.com'
    >>> browserHistory.back(2)
    'google.com'
    >>> browserHistory.back(7)
    'leetcode.com'
    """

    def __init__(self, homepage: str):
        self.back_history = [homepage]
        self.forward_history = []

    def visit(self, url: str) -> None:
        self.forward_history = []
        self.back_history.append(url)

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.back_history) > 1:
            self.forward_history.append(self.back_history.pop())
            steps -= 1
        return self.back_history[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.forward_history) > 0:
            self.back_history.append(self.forward_history.pop())
            steps -= 1
        return self.back_history[-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
