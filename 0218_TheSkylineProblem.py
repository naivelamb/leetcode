"""
https://leetcode.com/problems/the-skyline-problem/

For each building, we add (R, 0, float('inf)) to the array. Since this means there is another building from [R, float('inf')] with height 0.

We use a heapq to remember the current ending point of skyline and height. Highest and left-most building come first. 
When we are processing a new building, we need to pop all end points in the heap that are on the left of the current buildings. 
If current points has a non-zero height, we need to push its end point to heap. 
Finally, we need to process the sky line to results. 
"""
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = list({(R, 0, float('inf')) for _, R, _ in buildings})
        points += [(L, -H, R) for L, R, H in buildings]
        points.sort()

        res = [0, 0]
        heap = [[0, float('inf')]] # [-H, R]    
        for L, negH, R in points:
            while L >= heap[0][1]:
                heapq.heappop(heap)
            if negH != 0:
                # new skyline
                heapq.heappush(heap, [negH, R])
            if res[-1][1] != -heap[0][0]:
                res += [[L, -heap[0][0]]]    
        return res[1:]