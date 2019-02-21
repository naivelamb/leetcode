# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/shortest-palindrome/

#1 Brute Force
O(n^2)
"""
class Solution:
    def shortestPalindrome(self, s: 'str') -> 'str':
        ref = s[::-1]
        for i in range(len(ref)):
            if s.startswith(ref[i:]):
                return ref[:i] + s
        return ref + s
