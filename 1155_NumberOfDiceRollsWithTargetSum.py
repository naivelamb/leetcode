"""
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
DP[i][j] means rolled i dices, sum = j, num of rolls to reach such stat.
DP[i+1][k] = sum(DP[i][k-m] for m in range(1, f+1))

This can be solved by recursion. Use memo to avoid repeatation and be careful about target - f < 0.

Time complexity: O(d*f*target)
"""
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        def dp(d, target):
            if d == 0:
                return 0 if target > 0 else 1
            if (d, target) in memo:
                return memo[d, target]
            to_return = 0
            for k in range(max(0, target-f), target):
                to_return += dp(d-1, k)
            memo[d, target] = to_return
            return to_return
        return dp(d, target) % (10**9 + 7)

sol = Solution()
assert sol.numRollsToTarget(1,6,3) == 1
assert sol.numRollsToTarget(2,6,7) == 6
assert sol.numRollsToTarget(2,5,10) == 1
assert sol.numRollsToTarget(1,2,3) == 0
assert sol.numRollsToTarget(30,30,500) == 222616187
