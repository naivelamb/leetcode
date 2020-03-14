"""
https://leetcode.com/problems/longest-common-subsequence/

Dynamic Programming
DP[i][j] is the longest common subsequence for test1[:i], test2[:j]

if text1[i] == test2[j]: DP[i][j] = DP[i-1][j-1] + 1
else: DP[i][j] = max(DP[i][j-1], DP[i-1][j])

Time complexity: O(mn), m = len(text1), n = len(text2)
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                ans = max(dp[i][j], ans)
        return ans

sol = Solution()
assert sol.longestCommonSubsequence('abcde', 'ace') == 3
assert sol.longestCommonSubsequence('abc', 'abc') == 3
assert sol.longestCommonSubsequence('abc', 'def') == 0
