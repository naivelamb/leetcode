"""
https://leetcode.com/problems/summary-ranges/

Two pointer, merge range when nums[r] != nums[r-1] + 1
Time complexity: O(N)
"""
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if not nums:
            return ans
        if len(nums) == 1:
            return [str(nums[0])]
        
        l, r = 0, 1
        while r < len(nums):
            if nums[r] == nums[r-1] + 1:
                r += 1
            else:
                if r == l + 1:
                    ans.append(str(nums[l]))
                else:
                    ans.append(f"{nums[l]}->{nums[r-1]}")
                l = r
                r += 1
        
        if r == l + 1:
            ans.append(str(nums[l]))
        else:
            ans.append(f"{nums[l]}->{nums[r-1]}")
        return ans