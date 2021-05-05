"""
https://leetcode.com/problems/non-decreasing-array/

Greedy modify the number when encounter a non decreasing pair. 

Time complexity: O(N)
"""
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if cnt == 1:
                    return False
                cnt += 1
                if i < 2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return True