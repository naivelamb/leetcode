"""
https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/

It is same as find longest palindrome subsequences from w1+w2, but need to make sure the start is in (0, n1) and end is in (n1, n), where n1=len(word1), n=len(word1) + len(word2).

DP[i][j] => maximum palindrome subsequences for w[i:j+1]

if s[i] == s[j] (i!=j), DP[i][j] = 2 + DP[i+1][j-1]
else, DP[i][j] = max(DP[i][j-1], DP[i+1][j])

We only count ans when i < len(word1) and j >= len(word1)

Time complexity: O((m+n)^2)
"""
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        if s == s[::-1]:
            return len(s)
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        ans = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                    if i < len(word1) and j >= len(word2):
                        ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return ans