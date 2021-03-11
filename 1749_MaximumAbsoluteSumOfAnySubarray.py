"""
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

First try to find the maximum sum of subarray. 
Let dp[i] be the maximum sum of subarray ending with nums[i].
if dp[-1] < 0, dp[i] = nums[i]
else dp[i] = max(0, dp[-1] + nums[i])

Then make all element (0 - x) and do it again. 

Time complexity: O(2n)

"""
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        dp, ans = [-1], 0
        for x in nums:
            if dp[-1] < 0:
                dp.append(x)
            else:
                dp.append(max(0, dp[-1] + x))
            ans = max(ans, dp[-1])
        
        dp = [-1]
        for x in nums:
            x = -x
            if dp[-1] < 0:
                dp.append(x)
            else:
                dp.append(max(0, dp[-1] + x))
            ans = max(ans, dp[-1])
        
        return ans