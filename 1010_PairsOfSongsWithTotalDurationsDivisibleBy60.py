# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

Two sum, target => 60.

Time complexity: O(n)
"""
class Solution:
    def numPairsDivisibleBy60(self, time):
        ans, ref = 0, {}
        for x in time:
            x = x % 60
            ans += ref.get(x, 0)
            if x == 0:
                ref[x] = ref.get(x, 0) + 1
            else:
                ref[60 - x] = ref.get(60 - x, 0) + 1
        return ans
