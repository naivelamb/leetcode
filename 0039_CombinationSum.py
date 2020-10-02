"""
https://leetcode.com/problems/combination-sum/

Backtracking.

Time Complexity: O((n+k)!), k is the max repeated times for each candidates.
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def helper(candidates, target, curr, idx):
            if target == 0:
                ans.append(curr[:])
                return

            if target < 0:
                return

            for i in range(idx, len(candidates)):
                curr.append(candidates[i])
                helper(candidates, target - candidates[i], curr, i)
                curr.pop()

        helper(candidates, target, [], 0)
        return ans
