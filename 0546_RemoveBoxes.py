# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/remove-boxes/

dp[i][j][k] => max score of subarray b[i] ~ b[j] if there are k boxes that have
 the same color as b[j] following b[j].
dp[i][j][k] = dp[i][j-1][0] + (k + 1)^2           | Case 1: drop box[j], remove k + 1 boxes
            = dp[i][p][k+1] + dp[p+1][j-1][0]     | Case 2: Try all breakpoints p, b[p] == b[j]
"""
class Solution:
    def removeBoxes(self, boxes: 'List[int]') -> 'int':
        memo = {}
        
        def dp(i, j, k):
            if i > j: return 0
            while i < j and boxes[j - 1] == boxes[j]:
                j -= 1
                k += 1
            if (i, j, k) not in memo:
                ans = dp(i, j - 1, 0) + (k + 1) ** 2
                for p in range(i, j):
                    if boxes[j] == boxes[p]:
                        ans = max(ans, dp(i, p, k + 1) + dp(p + 1, j - 1, 0))
                memo[i, j, k] = ans
            return memo[i, j, k]
        
        return dp(0, len(boxes) - 1, 0)

s = Solution()
boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
print(s.removeBoxes(boxes))