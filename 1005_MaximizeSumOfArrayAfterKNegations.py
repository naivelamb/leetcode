# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

Find all negative, flip them as much as possible. (store in a min-heap)
If K is used up, return the sum.
Else, check how many K is remain. 
If K % 2 == 0 or min(A) == 0, return sum(A)
Else, return sum(A) - 2 * min(A)

So we first heapify A. As long as K > 0 and A[0] < 0, we pop one element from
A, flip it and push it back, K -= 1.

If K == 0 or K % 2 == 0 or A[0] == 0, return sum(A)
Else, return sum(A) - 2 * A[0]

Time complexity: O(nlogn)
"""
import heapq
class Solution:
    def largestSumAfterKNegations(self, A, K):
        heapq.heapify(A)
        while K > 0 and A[0] < 0:
            val = heapq.heappop(A)
            heapq.heappush(A, -val)
            K -= 1
        if K ==0 or K % 2 == 0 or A[0] == 0:
            return sum(A)
        else:
            return sum(A) - 2 * A[0]
