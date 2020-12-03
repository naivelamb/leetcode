"""
https://leetcode.com/problems/super-egg-drop/

f(M, K) denotes the given M moves and K eggs, what is the most number of floors we can solve. 
Hence we know
f(M, K) = f(M-1, K-1) + f(M-1, K) + 1

f(M, 1) = M when M >= 1
f(1, K) = 1 when K >= 1

Use 2D DP to sovle it.
Time complexity: O(KlogN)
Space complexity: O(KN)
"""

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][k] >= N:
                return m