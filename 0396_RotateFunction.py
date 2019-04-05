# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/rotate-function/

f(i) = sum(j*B_i[j])
f(i+1) = 1*B_i[0] + 2*B_i[1] + ... + k*B_i[k-1] + 0*B_i[k]  

f(i+1) - f(i) = sum(B_i[j]) - k*B_i[k] 
f(i+1) = f(i) + sum(array) - k*B_i[k]

Time complexity: O(n)
"""
class Solution:
    def maxRotateFunction(self, A) -> int:
        res = curr = sum(i*j for i, j in enumerate(A))
        total = sum(A)
        n = len(A)
        while A:
            curr += total - A.pop()*n
            res = max(res, curr)
        return res
