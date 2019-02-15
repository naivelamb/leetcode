# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/power-of-three/

Loop, keep dividing 3, until non-divisible, see whether we get 1. 
"""
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        
        while n % 3 == 0:
            n //= 3
        
        return n == 1
