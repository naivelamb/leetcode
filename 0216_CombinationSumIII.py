"""
https://leetcode.com/problems/combination-sum-iii/
Backtracking
Time Complexity: O(9!*K/(9-K)!)
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        nums = [x for x in range(1, 10)]
        if n > sum(nums[-k:]):
            return []
        if n == sum(nums[-k:]):
            return [nums[-k:]]
        self.helper(nums, 0, k, n, [], 0)
        return self.res

    def helper(self, nums, d, m, target, chosen, idx):
        if d == m and target == 0:
            self.res.append(list(chosen))
        if target < 0 or d > m:
            return

        for i in range(idx, len(nums)):
            chosen.append(nums[i])
            self.helper(nums, d+1, m, target - nums[i], chosen, i+1)
            chosen.pop()
