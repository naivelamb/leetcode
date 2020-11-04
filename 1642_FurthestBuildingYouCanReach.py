"""
https://leetcode.com/problems/furthest-building-you-can-reach/

1. DFS, record the remain bricks and ladders at each position.

Time compleixty: O(2^N)

2. PriorityQueue, record the difference, stop when len(heap) > ladders, try to use bricks. 

Time complexity: O(NlogK), K = ladders
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

    def furthestBuilding_pq(self, heights: List[int], bricks: int, ladders: int) -> int: 
        heap = []
        for i in range(1, len(heights)):
            d = heights[i] - heights[i-1]
            if d > 0:
                heapq.heappush(heap, d)
                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)
                    if bricks < 0:
                        return i - 1
        return len(heights) - 1