# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/next-greater-element-ii/

Brute force O(n^2)

We can extend nums to nums + nums, then return the next greater element result
for the first part, this avoid dealing with circular. 

We only need to remember the number and its next greater, all element smaller 
than the number can be ignored. => use stack to maintain this.

Time complexity: O(n)
"""
class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        # extend nums
        nums += nums
        res, stack = [], []
        for x in nums[::-1]:
            while stack and stack[-1] <= x:
                stack.pop()
            if not stack:
                res.append(-1)
            else:
                res.append(stack[-1])
            stack.append(x)
        res = res[::-1]
        return res[:n]
            
