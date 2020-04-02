"""
https://leetcode.com/problems/single-number/
"""
class Solution:
    def singleNumber(self, nums) -> int:
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
        for n in cnt:
            if cnt[n] == 1:
                return n

sol = Solution()
assert sol.singleNumber([2,2,1]) == 1
assert sol.singleNumber([4,1,2,1,2]) == 4
