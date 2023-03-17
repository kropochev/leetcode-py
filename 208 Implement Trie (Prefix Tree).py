class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False


class Trie:
    """
    A trie (pronounced as "try") or prefix tree is a tree data structure used
    to efficiently store and retrieve keys in a dataset of strings.
    There are various applications of this data structure, such as autocomplete
    and spellchecker.

    Implement the Trie class:
    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string word into the trie.
    - boolean search(String word) Returns true if the string word
    is in the trie (i.e., was inserted before), and false otherwise.
    - boolean startsWith(String prefix) Returns true if there is a previously
    inserted string word that has the prefix prefix, and false otherwise.

    >>> trie = Trie()
    >>> trie.insert("apple")
    >>> trie.search("apple")
    True
    >>> trie.search("app")
    False
    >>> trie.startsWith("app")
    True
    >>> trie.insert("app")
    >>> trie.search("app")
    True
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = ord(word[level])-ord("a")

            if not pCrawl.children[index]:
                pCrawl.children[index] = TrieNode()
            pCrawl = pCrawl.children[index]

        pCrawl.isEndOfWord = True

    def search(self, word: str) -> bool:
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = ord(word[level])-ord("a")
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        root = self.root

        for i in range(len(prefix)):
            index = ord(prefix[i])-ord("a")
            if (not root.children[index]):
                return False
            root = root.children[index]

        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
