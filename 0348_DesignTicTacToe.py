# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/design-tic-tac-toe/

#1 O(n) Solution:
Check row, col, diagonal, O(4n)

#2 O(1) Solution
Since all move is valid, we only need to remember the count of player in each 
row/col/diagonal. At every move, we check all the associated row/col/diagonal. 
"""

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = {i: [0, 0] for i in range(n)}
        self.cols = {i: [0, 0] for i in range(n)}
        self.diags = {0: [0, 0], 1: [0, 0]}
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.rows[row][player - 1] += 1
        self.cols[col][player - 1] += 1
        cnt = [self.rows[row][player - 1], self.cols[col][player - 1]]
        if row == col:
            self.diags[0][player - 1] += 1
            cnt.append(self.diags[0][player - 1])
        if row + col == self.n - 1:
            self.diags[1][player - 1] += 1
            cnt.append(self.diags[1][player - 1])
        if any(x == self.n for x in cnt):
            return player
        else:
            return 0
        
