# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/interval-list-intersections/

Two pointers. 
Do intersection between the interval. 
Keep the interval with larger end, and move the other forward
Time complexity: O(m + n), m = len(A), n = len(B)
"""

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        def merge(a, b):
            # get intersection of two intervals. 
            l = max(a.start, b.start)
            r = min(a.end, b.end)
            res = []
            if l <= r:
                res = [l, r]
            return res
        ans = []
        i, j = 0, 0
        m, n = len(A), len(B)
        while i < m and j < n:
            a, b = A[i], B[j]
            res = merge(a, b)
            if res:
                ans.append(res)
            if a.end < b.end:
                i += 1
            else:
                j += 1
        return ans