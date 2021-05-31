# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/maximum-gap/

#1 Naive way
Sort then compare neighbors, O(nlogn)

#2 bucket sort
If there are n numbers, put them into (n-1) buckets. Record max and min of each bucket. The maximum gap must be the difference between neighboring min & max. 

Time complexity: O(n)
"""
import collections


class Solution:
    def maximumGap(self, nums: 'List[int]') -> 'int':
        if len(nums) <= 1:
            return 0
        nums.sort()
        ans = 0
        for i in range(1, len(nums)):
            ans = max(ans, nums[i] - nums[i - 1])
        return ans

    def maximumGap_bucket(self, nums: 'List[int]') -> 'int':
        lo, hi, n = min(nums), max(nums), len(nums)
        if n <= 2 or lo == hi: return hi - lo
        B = collections.defaultdict(list)
        for num in nums:
            ind = n - 2 if num == hi else (num - lo) * (n - 1) // (hi - lo)
            B[ind].append(num)
        
        cands = [[min(B[i]), max(B[i])] for i in range(n - 1) if B[i]]
        return max(y[0] - x[1] for x, y in zip(cands, cands[1:]))