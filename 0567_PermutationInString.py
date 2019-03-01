# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/permutation-in-string/

Sliding window + hashmap to remember the count of characters in the window. 
Time Complexity: O(n)
"""
import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        ref = collections.Counter(s1)
        cnt = n1
        
        for i in range(n2):
            if i < n1:
                if s2[i] in ref:
                    ref[s2[i]] -= 1
                    if ref[s2[i]] >= 0:
                        cnt -= 1
            else:
                old_ch, new_ch = s2[i-n1], s2[i]
                if old_ch in ref:
                    ref[old_ch] += 1
                    if ref[old_ch] > 0:
                        cnt += 1
                if new_ch in ref:
                    ref[new_ch] -= 1
                    if ref[new_ch] >= 0:
                        cnt -= 1
            if cnt == 0:
                return True
        return False
