# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/complement-of-base-10-integer/

#1 convert to binary string, then change digit by digit. 
Time complexity: log(n)

#2 find the first 1111....111 > N, return X - N
Time complexity: log(n)
"""
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        vals = bin(N)[2:]
        res = []
        for x in vals:
            if x == '1':
                res.append('0')
            else:
                res.append('1')
        return int(''.join(res), 2)
    
    def bitwiseComplement_2(self, N):
        X = 1
        while X < N:
            X = X * 2 + 1
        return X - N

