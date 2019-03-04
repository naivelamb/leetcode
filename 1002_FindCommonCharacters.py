# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/find-common-characters/

Use dictionary to record the letters and their count in the first word.
Compare it with the rest.

Time Comlexity: O(mn), m -> length of word, n -> total words 
"""
class Solution:
    def commonChars(self, A):
        ref = {}
        for ch in A[0]:
            ref[ch] = ref.get(ch, 0) + 1
        
        for w in A[1:]:
            tmp = {}
            for ch in w:
                tmp[ch] = tmp.get(ch, 0) + 1
            for ch in ref:
                if ch not in tmp:
                    ref[ch] = 0
                else:
                    ref[ch] = min(ref[ch], tmp[ch])
        
        ans = []
        for key in ref:
            ans += [key] * ref[key]
        return ans
