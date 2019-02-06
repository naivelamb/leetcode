# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/meeting-rooms-ii/

Simulation. Sort the intervals based on start. 
Use a heap to remember the ending time of current on-going meeting.
When a new meeting comes in, 'empty' the rooms whose meeting has ended.
"""

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x.start)
        heap = [intervals[0].end]
        ans = 1
        for meeting in intervals[1:]:
            start, end = meeting.start, meeting.end
            while heap and start >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
            ans = max(ans, len(heap))
        return ans

s = Solution()
tests = [[0, 30],[5, 10],[15, 20]]
ints = []
for t in tests:
    ints.append(Interval(t[0], t[1]))
print(s.minMeetingRooms(ints))