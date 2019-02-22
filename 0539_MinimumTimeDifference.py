# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/minimum-time-difference/

Convert time to minutes, sort then compare neighbor. 
Ans is initiated to be timePoints[0] + 24 * 60 - timePoints[-1]
Time Complexity: O(nlogn)
"""
class Solution:
    def findMinDifference(self, timePoints: 'List[str]') -> 'int':
        timePoints = [list(map(int, x.split(':'))) for x in timePoints]
        timePoints = sorted([x[0] * 60 + x[1] for x in timePoints])
        ans = timePoints[0] + 24 * 60 - timePoints[-1]
        for i in range(1, len(timePoints)):
            ans = min(ans, timePoints[i] - timePoints[i - 1])
        return ans
    
s = Solution()
t = ["23:59", "00:00"]
print(s.findMinDifference(t))