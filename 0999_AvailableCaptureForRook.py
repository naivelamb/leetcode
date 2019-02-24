# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/available-captures-for-rook/

Find the Rook, check all 4 directions

Time Complexity: O(m*n)
"""
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    Rx, Ry = i, j
                    break
        
        ans = 0
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            i, j = Rx, Ry
            while 0 <= i + dx < m and 0 <= j + dy < n and board[i + dx][j + dy] not in 'BbP':
                i, j = i + dx, j + dy
                if board[i][j] == 'p':
                    ans += 1
                    break
        return ans
