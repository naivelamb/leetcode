"""
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

Sort the array based on the right position. Then we check balloons one by one, if the balloon left position is on the left of current arrow position, we continue; else, we update arrow position to the curretn balloon right position, and add one arrow.

Time compelxity: O(NlogN)
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda x: x[1])
        p, ans = points[0][1], 1
        for p1, p2 in points[1:]:
            if p1 <= p:
                continue
            ans += 1
            p = p2
        return ans
