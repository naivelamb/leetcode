# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-repeating-character-replacement/

Two-pinter, count the different letter in the window. 

Time complexity: O(n), n -> len(s)
"""
class Solution:
    def characterReplacement(self, s, k):
        ans = 0
        count = collections.defaultdict(int)
        left = 0
        for right, num in enumerate(s):
            count[num] += 1
            while right - left + 1 - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans        
        
