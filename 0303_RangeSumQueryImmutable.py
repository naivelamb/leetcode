# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/range-sum-query-immutable/

Build prefix sum in the __init__()
"""
class NumArray:

    def __init__(self, nums: 'List[int]'):
        self.psums = [0]
        for n in nums:
            self.psums.append(n + self.psums[-1])

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        return self.psums[j+1] - self.psums[i]
