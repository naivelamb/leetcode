"""
https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

Get prefix sum of candiesCount, 
dp[i] => total number of candies for candies[:i]

for a type, day, cap, to eat the type on the day,
dp[type] // cap <= day ==> make sure before the day, all previous candies can be eaten
dp[type + 1] > day ==> make sure we have the type to eat on the day. 

Time complexity: O(N)
"""
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        dp = [0]
        for c in candiesCount:
            dp.append(dp[-1] + c)
        
        ans = []
        for c_type, day, cap in queries:
            if dp[c_type] // cap <= day < dp[c_type + 1]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans