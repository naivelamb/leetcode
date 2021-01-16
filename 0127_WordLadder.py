"""
https://leetcode.com/problems/word-ladder/
BFS, change one char a time, avoid visited. 

"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0
        ref = set(wordList)
        if endWord not in ref:
            return 0
        queue = collections.deque([[beginWord, 1]])
        visited = set()
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + ch + word[i+1:]
                    # remove duplicate
                    if new_word in ref and new_word not in visited:
                        queue.append([new_word, step + 1])
                        visited.add(new_word)
        return 0