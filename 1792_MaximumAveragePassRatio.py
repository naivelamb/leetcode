"""
https://leetcode.com/problems/maximum-average-pass-ratio/

For each pair, compute benefit after addint the student to the class. 
Then do extraStudents update. 

Time compleixty: O(klogn), k = extraStudents, n = len(classes)
"""
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [(p/t - (p + 1)/(t+1), p, t) for p, t in classes]
        heapq.heapify(heap)
        while extraStudents:
            _, p, t = heapq.heappop(heap)
            heapq.heappush(heap, ((p+1)/(t+1) - (p+2)/(t+2), p+1, t+1))
            extraStudents -= 1

        ans = sum(p/t for _, p, t in heap)/len(heap)
        return ans