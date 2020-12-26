"""
https://leetcode.com/problems/decode-ways/

DP[i][0] => # of decode ways decode (i)-th digit as a letter.
DP[i][1] => # of decode ways deocde (i-1) & (i) together. 

If s[i] != '0', DP[i][0] = DP[i-1][0] + DP[i-1][1]
Else, DP[i][0] = 0
If 1<= int(s[i-1] + s[i]) <= 26, DP[i][1] = DP[i-2][0] + DP[i-2][1]

Be careful about the case if s[i-1] == '0'.

Time complexity: O(N), N = len(s)
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [[0, 0] for _ in range(N)]
        if s[0] != '0':
            dp[0][0] = 1
        for i in range(1, N):
            if s[i] != '0':
                dp[i][0] = dp[i-1][0] + dp[i-1][1]
            else:
                dp[i][0] = 0
            if s[i-1] != '0' and (0 < int(s[i-1:i+1]) <= 26):
                dp[i][1] = sum(dp[i-2]) if i >= 2 else 1
        return sum(dp[-1])