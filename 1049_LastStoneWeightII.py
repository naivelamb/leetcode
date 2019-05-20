# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/last-stone-weight-ii/

A stone can be added or substrated. We need to find the min of abs(sum) for all
the methods of processing stones.

Time complexity: O(2^n), since each stone has two processing ways.
"""

class Solution:
    def lastStoneWeightII(self, stones) -> int:
        dp = {0}
        for x in stones:
            dp = {a + x for a in dp} | {a - x for a in dp}
        return min(abs(x) for x in dp)