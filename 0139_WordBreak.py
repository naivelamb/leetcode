# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/word-break/

dp[i] => if s[:i] can be broken.
To comput dp[j] need all i such that i < j, check s[i:j] in wordDict or not.
"""
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n + 1)
        ids = [0]
        ref = set(wordDict)
        for j in range(1, n + 1):
            for i in ids:
                if s[i:j] in ref:
                    ids.append(j)
                    dp[j] = True
                    break
        return dp[-1]