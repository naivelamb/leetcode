"""
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

Consider the most general case, the array looks like
|.....|.....|.....|
   A     B     C

A and C are sorted, B is not. 
min(B) > max(A)
max(B) < min(C)

1). Search from left to right, to find the ending point of B. 
Record current max, if nums[i] >= current_max, current_max = nums[i], else r = i
2). Search from right to left, to find the starting point of B.
Record current min, if nums[i] <= current_min, current_min = nums[i], else l = i
If l == r: return 0
Return max(0, r - l + 1)

Time complexity: O(N)
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        m = nums[0]
        r = 0
        for i in range(1, len(nums)):
            if nums[i] >= m:
                m = nums[i]
            else:
                r = i
        m = nums[-1]
        l = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= m:
                m = nums[i]
            else:
                l = i
        
        if l == r:
            return 0
        else:
            return max(r - l + 1, 0)