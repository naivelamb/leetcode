# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/number-of-enclaves/

DFS, start from the boundary, mark all connected land as '#'. Then go over the 
board again, find count of '1'.

Time complexity: O(mn)
"""
class Solution:
    def numEnclaves(self, A):
        self.A = A
        m, n = len(A), len(A[0])
        def dfs(i, j):
            # A[i][j] is 1 starting from the boudnary
            # mark all neighbors connected to it as '#'
            self.A[i][j] = '#'
            dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and self.A[x][y] == 1:
                    dfs(x, y)

        for i in range(m):
            if self.A[i][0] == 1:
                dfs(i, 0)
            if self.A[i][n-1] == 1:
                dfs(i, n-1)                    
                    
        for j in range(n):
            if self.A[0][j] == 1:
                dfs(0, j)
            if self.A[m-1][j] == 1:
                dfs(m-1, j)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if self.A[i][j] == 1:
                    ans += 1
        return ans
