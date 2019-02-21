# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/minimum-window-substring/

Sliding window, record count of target characters in the window. 
Once match, shrink the left. 

Time Complexity: O(n)
"""
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ref = {}
        for ch in t:
            ref[ch] = ref.get(ch, 0) + 1
        window = ""
        count = len(t)
        if len(t) > len(s):
            return window
        
        l, r = 0, 0
        for r in range(len(s)):
            if s[r] in ref:
                ref[s[r]] -= 1
                if ref[s[r]] >= 0:
                    count -= 1
            if count == 0: # find matched string, now move left
                while count == 0:
                    if s[l] in ref:
                        ref[s[l]] += 1
                        if ref[s[l]] > 0:
                            count += 1
                    l += 1
                if not window or r - l + 1 < len(window):
                    window = s[l-1: r + 1]
        return window