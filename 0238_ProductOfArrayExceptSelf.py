# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/product-of-array-except-self/

Two dps, pre-product and after-product
"""

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        dp1 = [1] * n
        dp2 = [1] * n
        for i in range(1, n):
            dp1[i] = dp1[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            dp2[i] = dp2[i + 1] * nums[i + 1]
        
        res = []
        for i in range(n):
            res.append(dp1[i] * dp2[i])
        return res
