# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

If a letter has less than k count, then it can never be included in the substring. 
Therefore, we can split the string based on the letter, and the problem becomes
find the longest substring in all the substrings after splitting. 

Time complexity: O(nlogn)
"""
import collections
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        cnt = collections.Counter(s)
        for ch in cnt:
            if cnt[ch] < k:
                return max(self.longestSubstring(t, k) for t in s.split(ch))
        return len(s)