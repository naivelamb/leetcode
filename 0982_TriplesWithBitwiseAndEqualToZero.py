# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

First build the count dictionary. Key is the result of bitwize and of any two 
numbers in the array. 

Then we loop over the array again, compute the bitwise and with all keys in the
count dictionary, if the result is zero, ans += cnt[key].

Time complexity: O(n^3)
 
"""
class Solution:
    def countTriplets(self, A: 'List[int]') -> 'int':
        n = len(A)
        cnt = {}
        for i in range(n):
            for j in range(n):
                cnt[A[i] & A[j]] = cnt.get(A[i] & A[j], 0) + 1
        
        ans = 0
        for num in A:
            for v in cnt:
                if num & v == 0:
                    ans += cnt[v]
        return ans