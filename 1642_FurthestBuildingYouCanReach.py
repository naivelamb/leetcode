"""
https://leetcode.com/problems/furthest-building-you-can-reach/

DFS, record the remain bricks and ladders at each position.

Time compleixty: O(N)
"""
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int: 
        stack = [(0, bricks, ladders)]
        ans, n = 0, len(heights)
        while stack:
            i, bricks, ladders = stack.pop()
            ans = max(ans, i)
            if ans == n - 1:
                return ans
            if i < n:
                if heights[i] >= heights[i+1]: # no cost
                    stack.append((i+1, bricks, ladders))
                else:
                    delta = heights[i+1] - heights[i]
                    if ladders > 0:
                        stack.append((i+1, bricks, ladders - 1))
                    if bricks >= delta:
                        stack.append((i+1, bricks - delta, ladders))
        return ans