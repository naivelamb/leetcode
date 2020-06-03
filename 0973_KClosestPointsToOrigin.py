"""
https://leetcode.com/problems/k-closest-points-to-origin/

Compute distance to origin of all points, store them, heapify, then pop one by one.
Time complexity: O(2N + KlogN), N = # of points
"""
class Solution:
    def kClosest(self, points, K: int):
        dist = []
        for p1, p2 in points:
            dist.append((p1**2, p2**2, [p1, p2]))
        heapq.heapify(dist)
        ans = []
        for _ in range(K):
            _, p = heapq.heappop(dist)
            ans.append(p)
        return ans
