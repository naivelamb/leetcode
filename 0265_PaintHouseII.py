# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/paint-house-ii/submissions/

Let dp[i][j] be the min costs of painting i-th house with color j. 
Hence, we need a helper array min_list, where
min_list[i] = min(dp[i-1][:i] + dp[i-1][i+1:])

Then dp[i][j] = min_list[j] + costs[i][j]

Time complexity: O(nk)
Since the min_list can be got in O(k)
"""
class Solution:
    def minCostII(self, costs):
        def helper(costs):
            # given costs of length k, return a min_list,
            # where min_list[i] = min(costs[:i], costs[i+1:])
            # finish in O(k)
            k = len(costs)
            left_min = [float('inf')]
            for x in costs[:-1]:
                if x < left_min[-1]:
                    left_min.append(x)
                else:
                    left_min.append(left_min[-1])
            right_min = [float('inf')]
            for x in costs[k:0:-1]:
                if x < right_min[-1]:
                    right_min.append(x)
                else:
                    right_min.append(right_min[-1])
            right_min = right_min[::-1]
            ans = []
            for i in range(k):
                ans.append(min(left_min[i], right_min[i]))
            return ans
        
        if not costs or not costs[0]:
            return 0
        
        n = len(costs)
        k = len(costs[0])
        dp = costs[0]
        for i in range(1, n):
            pre_min = helper(dp)
            for j in range(k):
                dp[j] = costs[i][j] + pre_min[j]
        return min(dp)
