# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/spiral-matrix/

clockwise turn
"""
class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if not matrix or not matrix[0]:
            return []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        res = []
        i, j, d = 0, 0, 0
        while 0 <= i < m and 0 <= j < n and not visited[i][j]:
            res.append(matrix[i][j])
            visited[i][j] = True
            dx, dy = directions[d % 4]
            newi, newj = i + dx, j + dy
            if 0 <= newi < m and 0 <= newj < n and not visited[newi][newj]:
                i, j = newi, newj
            else:
                d += 1
                dx, dy = directions[d % 4]
                i, j = i + dx, j + dy
        return res
