"""
https://leetcode.com/problems/stone-game-iv/

#1 DFS
After Alice remove, if there remains 0 stons, the Alice loses. Given remaining n stones, we need to check if Alice remove k stones (where k is a square number) she can win or not. 
This becomes a recursion problem. ==> DFS
Time Complexity: O(N*N^0.5)

#2 DP
We can also use DP to solve the problem, where DP[i] means whether Alice could win if there remains i stones.
For every i, we need to check j in range [1, sqrt(i)] to find if any dp[i-j**2] is False, then dp[i] is True
Time complexity: O(N*N^0.5)
"""
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(maxsize=None)
        def dfs(n):
            if n == 0:
                return False
            k = int(n**0.5)
            for i in range(1, k+1):
                if not dfs(n-i**2):
                    return True
            return False
        return dfs(n)

    def winnerSquareGame_dp(self, n: int) -> bool:
        dp = [False] * (n+1)
        for i in range(1, n+1):
            for j in range(1, int(i**0.5) + 1):
                if not dp[i-j**2]:
                    dp[i] = True
                    break

        return dp[n]        