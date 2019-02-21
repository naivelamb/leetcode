# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/climbing-stairs/

DP. dp[i] -> # of ways to reach i
dp[i] = dp[i-1] + dp[i-2]
Time Complexity: O(n)
"""
class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
