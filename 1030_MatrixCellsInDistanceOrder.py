# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/matrix-cells-in-distance-order/

#1 sort
Time compelxity: O(nlogn)

#2 BFS
time complexity: O(n)
"""
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        res = [(abs(i - r0) + abs(j - c0), [i, j]) for i in range(R) for j in range(C)]
        res.sort()
        return [x[1] for x in res]
        
