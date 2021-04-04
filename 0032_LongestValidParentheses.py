"""
https://leetcode.com/problems/longest-valid-parentheses/

dp[i] => longest valid parentheses ending with s[i]

if s[i] == '(': pass
else:
    if s[i-1] == '(': dp[i] = 2 + dp[i-2]
    else:
        look back for dp[i-1]

time complexity: o(N)
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    if i == 1: dp[i] = 2
                    else: dp[i] = 2 + dp[i-2]
                else:
                    look_for = i - dp[i-1] - 1
                    if look_for >= 0 and s[look_for] == '(':
                        dp[i] = dp[i-1] + 2
                        if look_for - 1 >= 0:
                            dp[i] += dp[look_for - 1] 
        return max(dp)