"""
https://leetcode.com/problems/sum-of-all-subset-xor-totals/
"""
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for L in range(1, n + 1):
            for subset in itertools.combinations(nums, L):
                a = subset[0]
                for x in subset[1:]:
                    a = a^x
                ans += a
        return ans