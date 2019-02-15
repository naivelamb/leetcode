# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/range-sum-query-mutable/submissions/

Binary Index Tree
Store partial sum in each node and get total sum by traversing the tree from 
leaf to root. The tree has a height of log(n).
Query: O(log(n))
Update: O(log(n))

lowbit(x) = x & (-x)

Update tree: i += lowbit(i), i <= n.
Query tree: i -= lowbit(i), i > 0
"""
class BinaryIndexTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = [0] * (self.n + 1)
        self.sums = [0] * (self.n + 1)
        for i, v in enumerate(nums):
            self.update(i+1, v)
    
    def _lowbit(self, a):
        return a & -a
    
    def update(self, i, val):
        diff, self.nums[i] = val - self.nums[i], val
        while i <= self.n:
            self.sums[i] += diff
            i += self._lowbit(i)
    
    def get(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= self._lowbit(i)
        return res

class NumArray:

    def __init__(self, nums: 'List[int]'):
        self.bit = BinaryIndexTree(nums)
        
    def update(self, i: 'int', val: 'int') -> 'None':
        self.bit.update(i + 1, val)

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        return self.bit.get(j + 1) - self.bit.get(i)
        