"""
https://leetcode.com/problems/container-with-most-water/

Two pointer, move the lower one inward. 

Time complexity: O(N)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = maxArea = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxArea = max(maxArea, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea