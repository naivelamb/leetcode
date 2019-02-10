# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/add-to-array-form-of-integer/

Add K to A[-1], then keep carry.
"""
class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        A[-1] += K
        for i in range(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i:
                A[i - 1] += carry
        if carry:
            A = list(map(int, str(carry))) + A
        return A

s = Solution()
A = [1,2,0,0]
K = 34
print(s.addToArrayForm(A, K))
