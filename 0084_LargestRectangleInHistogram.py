"""
https://leetcode.com/problems/largest-rectangle-in-histogram/
left[i] => # of histograms consecutive >= heights[i] for any j <= i
right[i] => # of histograms consecutive >= heights[i] for any j >= i
For left[i], if we know heights[j] >= heights[i] and j < i, then we can move the pointer to i - left[j].
This would reduce the time complexity to O(N). 


Then the maximum rectangle using heights[i] has an area of
heights[i] * (left[i] + right[i] - 1)

Time complexity: O(N)
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        left = [1] * len(heights)
        for i in range(len(heights)):
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                left[i] += left[j]
                j -= left[j]
        
        right = [1] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            j = i + 1
            while j < len(heights) and heights[j] >= heights[i]:
                right[i] += right[j]
                j += right[j]
        
        ans = 0
        for i in range(len(heights)):
            tmp = heights[i] * (left[i] + right[i] - 1)
            ans = max(ans, tmp)
        return ans