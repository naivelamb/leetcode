# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/binary-prefix-divisible-by-5/

If we know the base-10 number if A[:i] is pre_num, then the base-10 number for 
A[:i+1] is pre_num * 2 + A[i]

Time complexity: O(n), n = len(A)
"""
class Solution:
    def prefixesDivBy5(self, A):
        res = []
        pre_num = 0
        for x in A:
            pre_num = pre_num * 2 + x
            res.append(pre_num % 5 == 0)
        return res
    
s = Solution()
A = [1,1,1,0,1]
print(s.prefixesDivBy5(A))
