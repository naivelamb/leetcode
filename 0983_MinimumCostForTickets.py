# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/minimum-cost-for-tickets/

dp[i+1][k] => lowest cost for days[i] if it is covered by costs[k]
0 -> 1 day pass
1 -> 7 day pass
2 -> 30 day pass 
"""

class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        n = len(days)
        dp = [[0]*3 for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = costs[0] + min(dp[i-1]) 
            j = i
            while j > 0 and days[i - 1] - days[j - 1] < 7:
                j -= 1
            dp[i][1] = costs[1] + min(dp[j])
            while j > 0 and days[i - 1] - days[j - 1] < 30:
                j -= 1
            dp[i][2] = costs[2] + min(dp[j])
        for t in dp:
            print(t)
        return min(dp[-1])
    
s = Solution()
days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2, 7, 15]
print(s.mincostTickets(days, costs))