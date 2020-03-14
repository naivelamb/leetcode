"""
https://leetcode.com/problems/decompress-run-length-encoded-list/
"""
class Solution:
    def decompressRLElist(self, nums):
        ans = []
        for i in range(0, len(nums)//2):
            freq, val = nums[2*i], nums[2*i + 1]
            ans += freq * [val]
        return ans

sol = Solution()
assert sol.decompressRLElist([1,2,3,4]) == [2,4,4,4]
assert sol.decompressRLElist([1,1,2,3]) == [1,3,3]
