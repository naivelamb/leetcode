# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/non-overlapping-intervals/

Do it in a greedy way. First sort the array based on start. 
If prev.end > curr.start, overlap, one of the intervals must be removed. 
If prev.end > curr.end, we remove the previous one. Else we remove the current
one. 

Time complexity: O(nlogn)
"""
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x.start)
        prev, cnt = 0, 0
        for i in range(1, len(intervals)):
            if intervals[prev].end > intervals[i].start: # overlap
                if intervals[prev].end > intervals[i].end: # remove previous
                    prev = i
                cnt += 1
            else:
                prev = i
        return cnt
        
