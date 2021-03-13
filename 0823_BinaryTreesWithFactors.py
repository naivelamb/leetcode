"""
https://leetcode.com/problems/binary-trees-with-factors/

dp[i] => using i as root, number of binary sub tree. 

if k = m * n
dp[k] = sum(dp[m] * dp[k/m] for all possible m)

Time Complexity: O(nlogn + n^2)
"""
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = {}
        for a in sorted(arr):
            dp[a] = sum(dp[b] * dp.get(a//b, 0) for b in dp if a % b == 0) + 1
        
        return sum(dp.values()) % (10**9 + 7)