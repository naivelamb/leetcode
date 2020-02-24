"""
https://leetcode.com/problems/contiguous-array/
We only care about difference in count(0) and count(1).

Time complexity: O(N), N = len(nums)
"""
from collections import defaultdict
class Solution:
    def findMaxLength(self, nums) -> int:
        ans, cnt = 0, 0
        ref = {0: -1}
        for i, num in enumerate(nums):
            if num == 0:
                cnt -= 1
            else:
                cnt += 1
            if cnt in ref:
                ans = max(ans, i - ref[cnt])
            else:
                ref[cnt] = i
        return ans

sol = Solution()
assert sol.findMaxLength([0,0,1,0,0,0,1,1]) == 6
assert sol.findMaxLength([0,1]) == 2
assert sol.findMaxLength([0,1,0]) == 2
