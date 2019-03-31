# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/smallest-integer-divisible-by-k/

We know that:
    11 = 10 * 1 + 1
    111 = 10 * 11 + 1
    1111 = 10 * 111 + 1
Hence we can start from 1, keep going larger to check if any number formed by 
1 can be divisible by K. 

Let rem = 1, we keep doing rem = (rem*10 + 1) % K, until rem == 0.
If there is no such integer exisits, rem will duplicate.  

Time complexity: O(n), where n is the answer
"""
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K == 1:
            return 1
        cnt, rem = 1, 1
        seen = {1}
        while rem != 0:
            rem = (rem * 10 + 1) % K
            if rem in seen:
                return -1
            seen.add(rem)
            cnt += 1
        return cnt

