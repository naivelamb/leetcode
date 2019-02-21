# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/word-search/

DFS + backtracking
"""

class Solution:
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:#find start point
                    path = set()
                    path.add((i, j))
                    if self.dfs(board, i, j, path, word[1:]):
                        return True
        return False
    
    def dfs(self, board, i, j, path, word):
        if not word:
            return True
        
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = i + di, j + dj
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in path:
                if board[x][y] == word[0]:
                    path.add((x, y))
                    if self.dfs(board, x, y, path, word[1:]):
                        return True
                    path.remove((x, y))
        return False
                    