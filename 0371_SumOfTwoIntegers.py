# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/sum-of-two-integers/

For python the add function only works when
a*b>=0 , or
a < 0 and abs(a) > b > 0 (the negative number has a larger absolute value)
b < 0 and abs(b) > a > 0
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        def add(a, b):
            if not a or not b:
                return a or b
            return add(a^b, (a&b) << 1)
        
        if a*b < 0:
            if a > 0:
                return self.getSum(b, a)
            if add(~a, 1) == b: # -a == b
                return 0
            if add(~a, 1) < b: # -a < b
                return add(~add(add(~a, 1), add(~b, 1)), 1) # -add(-a, b)
        
        return add(a, b)