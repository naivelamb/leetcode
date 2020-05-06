"""
https://leetcode.com/problems/majority-element/
"""
class Solution:
    def majorityElement(self, nums) -> int:
        n = len(nums)
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
            if cnt[num] > n//2:
                return num

sol = Solution()
assert sol.majorityElement([3,2,3]) == 3
assert sol.majorityElement([2,2,1,1,1,2,2]) == 2
