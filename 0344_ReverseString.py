# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/reverse-string/

Two pointer, swap.
"""
class Solution:
    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def reverseString_recursion(self, s) -> 'None':
        def helper(start, end, ls):
            if start >= end:
                return
            ls[start], ls[end] = ls[end], ls[start]
            return helper(start+1, end-1, ls)
        return helper(0, len(s)-1, s)
