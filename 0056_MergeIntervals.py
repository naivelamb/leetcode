"""
https://leetcode.com/problems/merge-intervals/

Sort, then merge one by one.

Time complexity: O(NlogN)
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            prev_l, prev_r = res.pop()
            curr_l, curr_r = intervals[i]
            if prev_r < curr_l:
                res += [[prev_l, prev_r], [curr_l, curr_r]]
            else:
                new_interval = [min(prev_l, curr_l), max(prev_r, curr_r)]
                res.append(new_interval)

        return res
