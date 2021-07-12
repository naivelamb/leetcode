"""
https://leetcode.com/problems/employee-free-time/

Sort all intervals, then merge intervals. The close intervals in between are answers. 

Time complexity: O(nlogn)
"""
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]': #O(nlogn)
        all_ints = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        res, pre = [], all_ints[0]
        for i in all_ints[1:]:
            if i.start <= pre.end:
                pre.end = max(i.end, pre.end)
            elif i.start > pre.end:
                res.append(Interval(pre.end, i.start))
                pre = i
        return res
    
    def employeeFreeTime_heap(self, schedule): # O(nlogk)
        heap = [(emp[0].start, emp[0].end, idx, 0) for idx, emp in enumerate(schedule)]
        heapq.heapify(heap)
        pre_s, pre_e = heap[0][0], heap[0][1]
        res = []

        while heap:
            s, e, e_id, idx = heapq.heappop(heap)

            if pre_e < s:
                res.append(Interval(pre_e, s))
                pre_s = s,
                pre_e = e
            else:
                pre_e = max(pre_e, e)
            
            if idx + 1 < len(schedule[e_id]):
                idx += 1
                heapq.heappush(heap, (schedule[e_id][idx].start, schedule[e_id][idx].end, e_id, idx))
        return res
        
        