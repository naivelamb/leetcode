"""
https://leetcode.com/problems/closest-dessert-cost/

m = len(baseCosts)
n = len(toppingCosts)

Get all possible toppingCosts ==> O(3^n)
Sort toppingCosts => O(n3^n)
For each base, binary search toppingCosts => O(mlogn + mn)
Overall time complexity: O(n3^n + mlogn + mn)
"""
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        possible_topping = set()
        def dfs(curr, i, nums):
            possible_topping.add(curr)
            if i == len(nums):
                return
            dfs(curr, i+1, nums)
            dfs(curr + nums[i], i+1, nums)
            dfs(curr + nums[i] * 2, i+1, nums)
        dfs(0, 0, toppingCosts)
        possible_topping = sorted(list(possible_topping))

        ans = float('inf')
        for v in baseCosts:
            idx = bisect.bisect_left(possible_topping, target - v)
            for di in [-1, 0, 1]:
                if 0 <= idx + di < len(possible_topping):
                    v_cand = possible_topping[idx+di]
                    if abs(v_cand + v - target) < abs(ans -target):
                        ans = v_cand + v
                    elif abs(v_cand + v - target) == abs(ans -target):
                        ans = min(v_cand + v, ans)
        return ans