# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Sliding window, cnt the characters in the window

Time Complexity: O(n)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        start, ans = 0, 0
        ref = {}
        for i, ch in enumerate(s):
            if ch in ref and start <= ref[ch]:
                start = ref[ch] + 1
            else:
                ans = max(ans, i - start + 1)
            ref[ch] = i
        return ans
            
