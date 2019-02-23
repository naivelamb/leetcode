# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/minimum-time-difference/

#1
Convert time to minutes, sort then compare neighbor. 
Ans is initiated to be timePoints[0] + 24 * 60 - timePoints[-1]
Time Complexity: O(nlogn)

#2 
Boolean array of 1440 (24 * 60)
Time Complexity: O(1440)
Better when n > 260
"""
class Solution:
    def findMinDifference(self, timePoints: 'List[str]') -> 'int':
        timePoints = sorted([int(x[:2]) * 60 + int(x[-2:]) for x in timePoints])
        ans = timePoints[0] + 24 * 60 - timePoints[-1]
        for i in range(1, len(timePoints)):
            ans = min(ans, timePoints[i] - timePoints[i - 1])
        return ans
    
    def findMinDifference_array(self, timePoints: 'List[str]') -> 'int':
        mask = [0] * 1440
        timePoints = [int(x[:2]) * 60 + int(x[-2:]) for x in timePoints]
        for t in timePoints:
            if not mask[t]:
                mask[t] = 1
            else:
                return 0
        
        ans = min(timePoints) + 1440 - max(timePoints)
        prev = None
        for i in range(len(mask)):
            if mask[i]:
                if not prev:
                    prev = i
                else:
                    ans = min(ans, i - prev)
                    prev = i
        return ans
        
s = Solution()
t = ["23:59", "00:00"]
print(s.findMinDifference(t))