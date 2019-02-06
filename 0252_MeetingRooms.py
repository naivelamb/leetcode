# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/meeting-rooms/

Sort the intervals based on starting time. Then compare the neighbors. 
Time Complexity: O(nlogn)
"""
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key = lambda x: x.start)
        
        for i in range(1, len(intervals)):
            l1, l2 = intervals[i-1], intervals[i]
            if l1.end > l2.start:
                return False
        return True

s = Solution()
starts = [0, 5, 15]
ends = [30, 10, 20]
ints = []
for i in range(len(starts)):
    inter = Interval(starts[i], ends[i])
    ints.append(inter)
print(s.canAttendMeetings(ints))