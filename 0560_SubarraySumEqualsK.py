"""
https://leetcode.com/problems/subarray-sum-equals-k/

Compute pre-sum. O(N)
For a pre-sum, p[i], we are looking for a (j > i), such that p[j] - p[i] == k.
So we need to go through the pre-sum again. O(N)

Time complexity: O(N)
"""
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        pre_sum = [0]
        for n in nums:
            pre_sum.append(pre_sum[-1] + n)
        ans = 0
        ref = {k: [0]}
        for i in range(1, len(pre_sum)):
            if pre_sum[i] in ref:
                ans += len(ref[pre_sum[i]])
            ref[pre_sum[i] + k] = ref.get(pre_sum[i] + k, []) + [i]
        return ans

sol = Solution()
assert sol.subarraySum([1,1,1], 2) == 2
