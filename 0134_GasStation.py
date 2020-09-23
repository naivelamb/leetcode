"""
https://leetcode.com/problems/gas-station/
Brute force: Try to start with every position, simulate it.
Time Complexity: O(N^2)

When we go through the position, we know the current start point is not possible when we found that there exists an i, such that,

1. For every j in (start, i), sum(gas[start:j+1]) - sum(cost[start:j+1]) > 0 ==> make sure we can reach i
2. sum(gas[start:i+1]) - sum(cost[start:i+1]) < 0 ==> we cannot go from i to i + 1.

When we found such a position, we know we cannot start from any point in the range [start, i], so we need to start from i + 1.
If (i + 1) could be the starting position, we need to make sure (i+1) could reach the end, and,
sum(gas[i+1:]) - sum(cost[i+1:]) + sum(gas[:i+1]) - sum(cost[:i+1]) >= 0

Time complexity: O(N)
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank, start, total = 0, 0, 0
        for i in range(n):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                total += tank
                tank = 0
        if total + tank < 0:
            return -1
        else:
            return start
