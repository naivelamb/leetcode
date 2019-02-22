# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/sudoku-solver/

DFS + backtracking
"""
class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, stack):
            # stack -> to be filled spot
            if not stack:
                return
            x, y = stack.pop()
            box = [board[x//3 + i][y//3 + j] for i in range(3) for j in range(3)]
            row = [board[x][j] for j in range(9)]
            col = [board[i][y] for i in range(9)]
            for i in '123456789':
                if not any([i in box, i in row, i in col]):
                    board[x][y] = i
                    dfs(board, stack)
                    if not stack:
                        return
            board[x][y] = '.'
            stack.append((x, y))
        
        stack = [(i, j) for i in range(9) for j in range(9) if board[i][j] == '.']
        dfs(board, stack)