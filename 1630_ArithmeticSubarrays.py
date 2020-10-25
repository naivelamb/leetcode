"""
https://leetcode.com/problems/arithmetic-subarrays/

Build the subarrays, sort then check. 

Time complexity: O(mlogn)
"""
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checkArithmetic(nums):
            if len(nums) == 2:
                return True
            delta = nums[1] - nums[0]
            for i in range(2, len(nums)):
                if nums[i] - nums[i-1] != delta:
                    return False
            return True
        
        ans = []
        for i in range(len(l)):
            ans.append(checkArithmetic(sorted(nums[l[i]: r[i]+1])))
        return ans