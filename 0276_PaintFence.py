# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/paint-fence/

@author: Xuan Cao
"""

class Solution:
    def numWays(self, n: 'int', k: 'int') -> 'int':
        if n == 0:
            return 0
        if n == 1:
            return k
        dp1, dp2 = [0] * n, [0] * n
        dp1[0] = dp2[0] = k
        dp1[1], dp2[1] = k, k*(k-1)
        for i in range(2, n):
            dp1[i] = dp2[i-1]
            dp2[i] = (dp1[i-1] + dp2[i-1]) * (k - 1)
        return dp1[-1] + dp2[-1]
    
s = Solution()
print(s.numWays(3, 2))