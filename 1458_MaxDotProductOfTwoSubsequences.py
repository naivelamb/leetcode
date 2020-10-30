"""
https://leetcode.com/problems/max-dot-product-of-two-subsequences/
DP[i][j] => max dot product of nums1[:i+1], nums2[:j+1].

DP[i][j] = max(dp[i-1][j-1] + nums1[i]*nums2[j], nums1[i] * nums2[j], dp[i][j-1], dp[i-1][j])

Time complexity: O(mn)
"""
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = ans = nums1[0] * nums2[0]
        for i in range(1, m):
            dp[i][0] = max(nums1[i] * nums2[0], dp[i-1][0])
            ans = max(ans, dp[i][0])
        for j in range(1, n):
            dp[0][j] = max(nums1[0] * nums2[j], dp[0][j-1])
            ans = max(ans, dp[0][j])
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i-1][j-1] + nums1[i] * nums2[j], nums1[i] * nums2[j], dp[i-1][j], dp[i][j-1])
                ans = max(ans, dp[i][j])
        
        return ans