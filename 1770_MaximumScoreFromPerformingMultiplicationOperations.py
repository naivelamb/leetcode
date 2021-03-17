"""
https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

DP[l, r, k] => for k th operation, we can choose from either nums[l] or nums[r], the maximum score.

DP[l, r, k] = max(nums[l] * multipliers[k] + DP[l+1, r, k+1], nums[r] * multipliers[k] + DP[l, r-1, k+1])

bottom-up dp.

Time complexity: O(m^2)

"""
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(2000)
        def dp(l, r, k):
            if k == len(multipliers): return 0
            return max(nums[l] * multipliers[k] + dp(l+1, r, k), nums[r] * multipliers[k] + dp(l, r-1, k))
        
        return dp(0, len(nums) - 1, 0)