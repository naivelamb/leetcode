# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/convert-to-base-2/

If we see a '1' at the odd position, we need to keep it and carry 1 to next 
digit.

Time complexity: O(n), where n is the length of answer
"""
class Solution:
    def baseNeg2(self, N: int) -> str:
        # convert to string
        vals = list(str(bin(N))[2:])
        vals = vals[::-1]
        
        i, carry = 0, 0
        while i < len(vals):
            tmp = int(vals[i]) + carry
            carry = tmp // 2
            vals[i] = str(tmp % 2)
            
            if i % 2 != 0 and vals[i] == '1':
                carry += 1
                
            i += 1
            
            if i == len(vals) and carry != 0:
                vals.append('0')
                
        return ''.join(vals[::-1])
