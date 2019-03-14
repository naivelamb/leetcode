# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/lexicographical-numbers/

#1
Convert to string, sort, then convert back

Time complexity: O(nlogn)
"""
class Solution:
    def lexicalOrder(self, n: int):
        vals = [str(x) for x in range(1, n + 1)]
        vals.sort()
        return [int(x) for x in vals]
