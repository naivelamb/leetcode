# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/path-sum-iv/

"""
class Solution:
    def pathSum(self, nums):
        vals, idxs, pos = [], [], {}
        for i, num in enumerate(nums):
            D = num // 100
            P = (num - D*100) // 10
            V = num % 10
            pos[(D, P)] = i
            idxs.append((D, P))
            vals.append(V)
        cnt = [0] * len(vals)
        visited = set()
        for (D, P) in idxs[::-1]:
            if (D, P) in visited:
                continue
            while D != 0 and P != 0:
                visited.add((D, P))
                cnt[pos[(D, P)]] += 1
                D -= 1
                P = (P+1)//2
        ans = 0
        for n, val in zip(cnt, vals):
            ans += n*val
        return ans

sol = Solution()
nums = [113, 215, 221]
assert sol.pathSum(nums) == 12

nums = [113, 221]
assert sol.pathSum(nums) == 4
