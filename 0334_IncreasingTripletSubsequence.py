# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/increasing-triplet-subsequence/

remember first and second min

Time complexity: O(n)
"""
class Solution:
    def increasingTriplet(self, nums):
        first = second = float('inf')
        
        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                return True
        return False
        
