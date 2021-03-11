"""
https://leetcode.com/problems/palindrome-partitioning-iv/

dp[i][k] => s[:i] can be divided in to k sub palindrome. 

dp[i][k] = True if for any j in (0, i),
dp[j][k-1] = True and s[j:i] == s[j:i][::-1]

dp[0][0] = True
dp[1][1] = True

Time complexity: O(3n^2)

"""
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * 4 for _ in range(n + 1)]
        dp[0][0], dp[1][1] = True, True
        for i in range(1, n + 1):
            for k in range(1, 4):
                for j in range(i):
                    if dp[j][k - 1] and s[i:j] == s[i:j][::-1]:
                        dp[i][k] = True
                        break
        return dp[-1][-1]