# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/best-sightseeing-pair/

A[i] + A[j] + i - j = A[i] + i + A[j] - j
Therefore, we can build two arrays from A, such that,
A1[i] = A[i] + i
A2[i] = A[i] - i
Then we are looking for i < j such that,
A1[i] + A2[j] is maximized. 

So we need to build a helper ref_dict, where,
ref_dict[i] = max(A2[i+1:])

Then we just need to loop over A1 and we can get the answer.

Time complexity: O(n), n = len(A)
"""
class Solution:
    def maxScoreSightseeingPair(self, A):
        A1 = [A[i] + i for i in range(len(A))]
        A2 = [A[i] - i for i in range(len(A))]
        ref = {len(A): -float('inf')}
        for i in range(len(A) - 1, -1, -1):
            ref[i] = max(A2[i], ref[i + 1])
        
        ans = -float('inf')
        for i in range(len(A)):
            ans = max(ans, A1[i] + ref[i + 1])
        return ans
