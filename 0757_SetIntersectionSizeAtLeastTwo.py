# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/set-intersection-size-at-least-two/

Return size of a set, not a interval.
Sort the intervals by end. Then we need to keep track of the right-most 2 elements
and use them as many as possible.

Time complexity: O(nlog(n)) 
"""
class Solution:
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: x[1])
        res = 0
        cur = []
        for start, end in intervals:
            if not cur or start > cur[1]:
                res += 2
                cur=[end-1,end]
            elif start > cur[0]:
                res += 1
                cur = [cur[1],end]

        return res


sol = Solution()

intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
assert sol.intersectionSizeTwo(intervals) == 3

intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
assert sol.intersectionSizeTwo(intervals) == 5
