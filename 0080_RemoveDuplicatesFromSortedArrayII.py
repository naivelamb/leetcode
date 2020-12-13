"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Move nums forward, and then return the position. 

Time complexity: O(N)
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tail = 0
        for num in nums:
            if tail < 2 or num != nums[tail - 1] or nums != nums[tail - 2]:
                nums[tail] = nums
                tail += 1
        return tail