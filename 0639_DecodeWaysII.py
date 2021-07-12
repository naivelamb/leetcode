"""
https://leetcode.com/problems/decode-ways-ii/


dp[i][0] => total of decode ways for s[:i+1]
dp[i][1] => total of decode ways for s[:i+1], ending with '1' and s[i] not used
dp[i][2] => total of decode ways for s[:i+1], ending with '2' and s[i] not used.
if s[i] != '*':
dp[i][0] = (s[i] > '0') * dp[i-1][0] + dp[i-1][1] + (s[i] <= '6') * dp[i-1][2]
dp[i][1] = (s[i] == '1') * dp[i-1][0]
dp[i][2] = (s[i] == '2') * dp[i-1][0]
if s[i] == '*':
dp[i][0] = 9 * dp[i-1][0] + 9 * dp[i-1][1] + 6 * dp[i-1][2]
dp[i][1] = dp[i-1][0]
dp[i][2] = dp[i-1][0]

Time complexity: O(N)
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [1, 0, 0]
        for c in s:
            dp_new = [0, 0, 0]
            if c == '*':
                dp_new[0] = 9 * dp[0] + 9 * dp[1] + 6 * dp[2]
                dp_new[1] = dp[0]
                dp_new[2] = dp[0]
            else:
                dp_new[0] = (c > '0') * dp[0] + dp[1] + (c <= '6') * dp[2]
                dp_new[1] = (c == '1') * dp[0]
                dp_new[2] = (c == '2') * dp[0]
            dp = [x % MOD for x in dp_new]
        return dp[0]        