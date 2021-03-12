"""
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

Find turning point, then iterate from it. 

Time complexity: O(N)
"""
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        flag = -1
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                flag = i
                break
        
        if flag == -1:
            return True
        
        i = flag + 1
        while i % n != flag:
            if nums[i % n] < nums[i % n -1]:
                return False
            i += 1
        return True