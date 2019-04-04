# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/data-stream-as-disjoint-intervals/

Maintain the intervals in a sorted order. When adding a number, its position 
can be found by binary search. Then we can decide whether to merge it with the 
neighbor intervals. 

Time complexity: Binary search O(logn), merge O(n), overall O(n)
"""
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SummaryRanges:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val: int) -> None:
        # find location
        l, r = 0, len(self.intervals) - 1
        while l <= r:
            mid = (l + r) // 2
            interval = self.intervals[mid]
            if interval.start <= val <= interval.end:
                return
            elif interval.start > val:
                r = mid - 1
            else:
                l = mid + 1
        
        # insert interval
        pos = min(l, r) + 1
        self.intervals[pos:pos] = [Intervals(val, val)]
        
        if pos + 1 < len(self.intervals) and val == self.intervals[pos+1].start - 1:
            self.intervals[pos].end = self.intervals[pos+1].end
            self.intervals[pos+1:pos+2] = []
        
        if pos - 1 >= 0 and val == self.intervals[pos-1].end + 1:
            self.intervals[pos-1].end = self.intervals[pos].end
            self.intervals[pos:pos+1] = []
    
    def getIntervals(self):
        return self.intervals
    