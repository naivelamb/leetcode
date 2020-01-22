# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/find-anagram-mappings/

Return size of a set, not a interval.
Sort the intervals by end. Then we need to keep track of the right-most 2 elements
and use them as many as possible.

Time complexity: O(nlog(n))
"""
import collections

class Solution:
    def anagramMappings(self, A, B):
        mapping = collections.defaultdict(list)
        for i, v in enumerate(B):
            mapping[v].append(i)

        res = []
        for v in A:
            res.append(mapping[v][-1])
            mapping[v].pop()
        return res


sol = Solution()

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
assert sol.anagramMappings(A, B) == [1, 4, 3, 2, 0]
