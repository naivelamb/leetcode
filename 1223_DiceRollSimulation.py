"""
https://leetcode.com/problems/dice-roll-simulation/


Let dp[i][j] be the number of sequences for i rolls, when we get j after the roll.
dp[i][faces] be the total number of unique sequences after i rolls.
Let's say rollMax[j] = k. Then we need to check every possible rollMax from 0 to k, and find the number. If we roll x consectutive j, then the number of sequences is,
dp[i-x][faces] - dp[i-x][j]

Therefore, dp[i][j] = sum(dp[i-x][faces] - dp[i-x][j]) for all x in range(1, rollMax[j]+1).

Time complexiy: O(mn), m = max(rollMax) 
"""
class Solution:
    def dieSimulator(self, n: int, rollMax) -> int:
        mod = 10**9 + 7
        faces = len(rollMax)
        dp = [[0]*(faces+1) for _ in range(n+1)]
        dp[0][faces] = 1
        for i in range(faces):
            dp[1][i] = 1
        dp[1][faces] = sum(dp[1])
        for i in range(2, n+1):
            for j in range(faces):
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        break
                    dp[i][j] += dp[i-k][faces] - dp[i-k][j]
            dp[i][faces] = sum(dp[i])

        return dp[n][faces] % mod

sol = Solution()
assert sol.dieSimulator(2, [1,1,2,2,2,3]) == 34
assert sol.dieSimulator(2, [1,1,1,1,1,1]) == 30
assert sol.dieSimulator(3, [1,1,1,2,2,3]) == 181
