"""
https://leetcode.com/problems/add-and-search-word-data-structure-design/

Use Trie to store the added words. Use DFS to search.

Time Comlexity:
addWord -- O(N), N = len(word)
searchWord -- O(26^N), N = len(word)
"""
class TrieNode:
    def __init__(self, char):
        self.val = char
        self.next = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for ch in word:
            if ch in curr.next:
                curr = curr.next[ch]
            else:
                curr.next[ch] = TrieNode(ch)
                curr = curr.next[ch]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(root, word):
            if len(word) == 1:
                if word == '.':
                    if any([root.next[x].end for x in root.next]):
                        return True
                    else:
                        return False
                else:
                    if word in root.next and root.next[word].end:
                        return True
                    else:
                        return False
            else:
                for ch in word:
                    if ch != '.':
                        if ch not in root.next:
                            return False
                        else:
                            return dfs(root.next[ch], word[1:])
                    else:
                        if any([dfs(root.next[x], word[1:]) for x in root.next]):
                            return True
                        else:
                            return False
        return dfs(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
