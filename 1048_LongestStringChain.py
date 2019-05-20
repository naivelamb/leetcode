# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-string-chain/

dp[s] -> length of the longest string chain ending with string s.
We need to check the substrings of the string exist or not.

Time complexity: O(nlogn + nm), n -> len(words), m -> len(word)
"""
class Solution:
    def longestStrChain(self, words) -> int:
        dp = {}
        for w in sorted(words, key=len):
            for i in range(len(w)):
                dp[w] = max(dp.get(w, 1), dp.get(w[:i] + w[i+1:], 0) + 1)
        return max(dp.values() or 1)