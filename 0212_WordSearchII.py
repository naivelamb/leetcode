"""
https://leetcode.com/problems/word-search-ii/

Use trie to represent the dictionary. Store word in the end node in the trie.
Use dfs to find all words, if a site is visited, mark it as '#', and change it back after finding all possible solutions. This could avioid use a site multiple times.
When we found a word, also change the end node to be false, to avioid infinte loop.


"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end=False
        self.word=''

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True
        curr.word = word

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True

class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        node = trie.root
        self.res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j)
        return self.res

    def dfs(self, board, node, i, j):
        if node.is_end:
            self.res.append(node.word)
            node.is_end = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        tmp = board[i][j]
        if tmp not in node.children:
            return
        node = node.children[tmp]
        board[i][j] = '#'
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            self.dfs(board, node, i+dx, j+dy)
        board[i][j] = tmp
