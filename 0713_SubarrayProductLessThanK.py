"""
https://leetcode.com/problems/subarray-product-less-than-k/
Let dp[i] = (j, v), where j is the smallest index such that v = prod(nums[j:i+1]) < k.

If nums[i] * dp[i-1] < k:
dp[i] = (dp[i-1][0], dp[i-1][1] * nums[i])
Else:
let j = dp[i-1][0] + 1, keep trying untill we find the smallest index.

Time Complexity: O(N)
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        dp = [(i, 1) for i in range(len(nums))]
        if nums[0] < k:
            dp[0] = (0, nums[0])
            ans = 1
        else:
            dp[0] = (1, -1)
            ans = 0

        for i in range(1, len(nums)):
            j, v = dp[i-1]
            if v == -1:
                if nums[i] < k:
                    dp[i] = (i, nums[i])
                    ans += 1
                else:
                    dp[i] = (i+1, -1)
            else:
                v *= nums[i]
                while v >= k and j <= i:
                    v /= nums[j]
                    j += 1
                if j > i:
                    dp[i] = (j, -1)
                else:
                    dp[i] = (j, v)
                    ans += i - j + 1
        return ans
