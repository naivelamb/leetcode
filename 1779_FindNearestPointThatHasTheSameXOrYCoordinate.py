"""
https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

Iterate through the list.
Time complexity: O(N)
"""
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist, ans = float('inf'), -1
        for i, p in enumerate(points):
            a, b = p
            d = abs(a - x) + abs(b - y)
            if (a == x or b == y) and d < dist:
                dist = d
                ans = i
        return ans