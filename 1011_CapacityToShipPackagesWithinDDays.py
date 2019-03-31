# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

The compacity should be in the range of max(weights), sum(weights). Use binary
search to find the value.

Time complexity: O(nlogw), n = len(weights), w = sum(weights) - max(weights)
"""
class Solution:
    def shipWithinDays(self, weights, D):
        left, right = max(weights), sum(weights)
        while left < right:
            # mid -> current compacity
            mid, need, cur = (left + right) // 2, 1, 0
            # how many bags we need?
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D: # compacity too low
                left = mid + 1
            else:
                right = mid
        return left