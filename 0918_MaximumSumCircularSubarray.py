"""
https://leetcode.com/problems/maximum-sum-circular-subarray/
"""
class Solution:
    def maxSubarraySumCircular(self, A) -> int:
        max_sub = self.helper(A)
        for i in range(len(A)):
            A[i] = -A[i]
        min_sub = -self.helper(A)
        total = sum(A)
        return max(max_sub, total - min_sub) if max_sub > 0 else max_sub

    def helper(self, A):
        ans, prev_sum = float('-inf'), 0
        for n in A:
            prev_sum = max(prev_sum, 0) + n
            ans = max(prev_sum, ans)
        return ans

    def maxSubarraySumCircular_1pass(self, A) -> int:
        total, maxSum, curMax, minSum, curMin = 0, -float('inf'), 0, float('inf'), 0
        for n in A:
            curMax = max(curMax + n, n)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + n, n)
            minSum = min(minSum, curMin)
            total += n
        return max(maxSum, total-minSum) if maxSum > 0 else maxSum


sol = Solution()
assert sol.maxSubarraySumCircular([1,-2,3,-2]) == 3
assert sol.maxSubarraySumCircular([5,-3,5]) == 10
assert sol.maxSubarraySumCircular([3,-1,2,-1]) == 4
assert sol.maxSubarraySumCircular([3,-2,2,-3]) == 3
