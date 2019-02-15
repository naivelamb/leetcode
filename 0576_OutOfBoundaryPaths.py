# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/out-of-boundary-paths/

# 3D dp
Let dp[k][i][j] be the number of ways to reach (i, j) at step-k. 
To get this dp array, we need dp[k-1][i][j], which is the information for step-(k-1)

The count of out-bound path for step-k is basically sum of paths along all boundary. 
And we need to sum this count for all steps.  

Time complexity: O(kmn), Space: O(mn) if using temp. 
"""
class Solution:
    def findPaths(self, m: 'int', n: 'int', N: 'int', i: 'int', j: 'int') -> 'int':
        mod = 10**9 + 7
        count = 0
        dp = [[0] * n for _ in range(m)]
        dp[i][j] = 1
        for _ in range(N):
            tmp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                        if 0 <= x < m and 0 <= y < n:
                            tmp[x][y] += dp[i][j]
                        else:
                            count = (count + dp[i][j]) % mod
            dp = tmp
        return count

s = Solution()
print(s.findPaths(2, 2, 2, 0, 0))