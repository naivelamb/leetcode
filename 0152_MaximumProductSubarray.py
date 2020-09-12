"""
https://leetcode.com/problems/maximum-product-subarray/

We need to record the min_val and max_val by using the specific n as the end element.

If n > 0, then max = n * max_val_prev
If n < 0, then max = n * min_val_prev
Of course, also need to compare with n itself.

Time Complexity: O(N)
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_val, max_val = nums[0], nums[0]
        ans = nums[0]
        for n in nums[1:]:
            min_val, max_val = min(n, n*min_val, n*max_val), max(n, n*min_val, n*max_val)
            ans = max(ans, max_val)
        return ans
