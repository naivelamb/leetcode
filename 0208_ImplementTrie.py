"""
https://leetcode.com/problems/implement-trie-prefix-tree/
"""
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                node.children[ch] = TrieNode(ch)
                node = node.children[ch]
        node.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        if node.end:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return True
