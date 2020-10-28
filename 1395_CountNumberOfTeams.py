"""
https://leetcode.com/problems/count-number-of-teams/
dp[f] = a, b
a -> number of i for i < j, rating[i] < rating[j]
b -> number of i for i < j, rating[i] > rating[j]

Then for each k, we need to check all j in [1, k-1],
if nums[k] > nums[j], ans += dp[j][0]
if nums[k] < nums[j], ans += dp[j][1]

Time complexity: O(N^2)
"""
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        dp = [[0, 0]]
        for j in range(1, len(rating)):
            a, b = 0, 0
            for i in range(0, j):
                if rating[i] < rating[j]: a += 1
                if rating[i] > rating[j]: b += 1
            dp.append([a, b])
        
        ans = 0
        for k in range(2, len(rating)):
            for j in range(1, k):
                a, b = dp[j]
                if rating[k] > rating[j]: ans += a
                if rating[k] < rating[j]: ans += b
        return ans        
