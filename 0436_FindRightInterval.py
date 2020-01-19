# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/find-right-interval/

Build an array, the element is (left_val, index), and sort it.
For each interval in the raw array, binary search the right_val to find the location.

Time complexity: O(nlog(n))
"""


class Solution:
    def findRightInterval(self, intervals):
        left = []
        for i, (l, r) in enumerate(intervals):
            left.append((l, i))
        left.sort()

        ans = []
        for d in intervals:
            ans.append(self.binary_search(d[1], left))
        return ans

    def binary_search(self, target, vals):
        if target > vals[-1][0] or target < vals[0][0]:
            return -1
        else:
            l, r = 0, len(vals) - 1
            while r - l > 1:
                m = (l+r)//2
                if vals[m][0] >= target:
                    r = m
                else:
                    l = m
            return vals[r][1]

sol = Solution()


intervals = [[1,2]]
assert sol.findRightInterval(intervals) == [-1]

intervals = [[3,4], [2,3], [1,2]]
assert sol.findRightInterval(intervals) == [-1, 0, 1]

intervals = [[1,4], [2,3], [3,4]]
assert sol.findRightInterval(intervals) == [-1, 2, -1]
