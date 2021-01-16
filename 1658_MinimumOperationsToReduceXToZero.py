"""
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

Get prefix sum of [nums + nums], then find the minimum subarray such that prefix[j] - prefix[i] == x.

Make sure (i, j) covers head or tail, and does not exceed len(nums)

Time complexity: O(N)
"""
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        pre_fix = [0]
        ref = {0:0}
        ans = float('inf')

        for i, c in enumerate(nums + nums):
            pre_fix.append(pre_fix[-1] + c)
            ref[pre_fix[-1]] = i + 1
            if pre_fix[-1] - x >= 0 and pre_fix[-1] - x in ref:
                l = ref[pre_fix[-1] - x]
                tmp = i + 1 - l
                if tmp > len(nums):
                    continue
                if l == 0 or i == len(nums) - 1 or l <= len(nums) - 1 < i:
                    ans = min(ans, tmp)
        
        return ans if ans < float('inf') else -1