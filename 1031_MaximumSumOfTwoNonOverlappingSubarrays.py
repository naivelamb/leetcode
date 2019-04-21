# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

First compute the array AL, where AL[i] = sum(A[i-L+1:i+1])
To get maximum sum of non-overlapping subarrays, we need two other helper arrays:
    AL1[i] = max(AL[:i+1])
    AL2[i] = max(AL[i:])
Then we can get the result by one scan.

Time complexity: O(n)
"""
class Solution:
    def maxSumTwoNoOverlap(self, A, L, M):
        def window_sum(A, L):
            # window sum of size L
            tmp = sum(A[:L])
            dp = [0] * (L - 1)
            dp.append(tmp)
            for i in range(L, len(A)):
                tmp = tmp - A[i-L] + A[i]
                dp.append(tmp)
            return dp
        
        def pre_max(A):
            # return pre_max form of A
            dp = [A[0]]
            for i in range(1, len(A)):
                dp.append(max(dp[-1], A[i]))
            return dp
        
        AL = window_sum(A, L)
        AM = window_sum(A, M)
        AM1 = pre_max(AM)
        AM2 = pre_max(AM[::-1])[::-1]
        
        ans = 0
        for i in range(len(A)):
            a = AL[i]
            b = 0 if i - L < 0 else AM1[i - L]
            c = 0 if i + M >= len(A) else AM2[i + M]
            ans = max(ans, a + b, a + c)
        return ans