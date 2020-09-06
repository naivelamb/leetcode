"""
https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/

Find consecutive repeating letters, then we keep the one with maximum cost.

Time Complexity: O(N)
"""
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans, i = 0, 1
        while i < len(s):
            if s[i] == s[i-1]:#duplicate
                v_max = tmp = cost[i-1]
                j = i
                while j < len(s) and s[j] == s[i-1]:
                    tmp += cost[j]
                    v_max = max(v_max, cost[j])
                    j += 1
                ans += tmp - v_max
                i = j
            else:
                i += 1
        return ans
