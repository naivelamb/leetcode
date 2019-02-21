# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/degree-of-an-array/

Save val-idx into hashmap, we know the degree of the array after storing.
Then we go through the hashmap, if we see a key has the frequency, then
length = ref[n][-1] - ref[n][0] + 1
"""
import collections
class Solution:
    def findShortestSubArray(self, nums: 'List[int]') -> 'int':
        ref = collections.defaultdict(list)
        freq = 0
        for i, n in enumerate(nums):
            ref[n].append(i)
            freq = max(freq, len(ref[n]))
        ans = len(nums)
        for n in ref:
            if len(ref[n]) == freq:
                ans = min(ans, ref[n][-1] - ref[n][0] + 1)
        return ans