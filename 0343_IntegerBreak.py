# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/integer-break/

2 -> 1+1 -> 1
3 -> 1+2 -> 2
4 -> 2+2 -> 4
5 -> 2+3 -> 6
6 -> 3+3 -> 9
7 -> 3+4 -> 12
8 -> 2+3+3 -> 18
9 -> 3+3+3 -> 27
10 -> 3+3+4 -> 36

Let's say f(n) gives the product of integers for n, then 
f(j) = max(i*(j-i), f(i)*(j-i)) for all possible i.
i*(j-i) => don't break i
f(i)*(j-i) => break i 

Time Complexity: O(n^2)
"""
class Solution:
    def integerBreak(self, n: 'int') -> 'int':
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(2, i + 1):
                dp[i] = max(dp[i], j * (i - j), dp[j]*(i - j))
        return dp[n]
