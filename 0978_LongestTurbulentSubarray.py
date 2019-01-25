# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-turbulent-subarray/

Use two dp arrays,
dp1[i] => longest subarray ending with A[i], with A[i] > A[i-1]
dp2[i] => longest subarray ending with A[i], with A[i] < A[i-1]

If A[i] > A[i-1], to make it turbulent, A[i-1] < A[i-2]
therefore, dp1[i] = dp2[i-1] + 1
If A[i] < A[i-1], to make it turbulent, A[i-1] > A[i-2]
therefore, dp2[i] = dp1[i-1] + 1

Check max(max(dp1), max(dp2))
"""
class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        dp1, dp2 = [1]*n, [1]*n
        for i in range(1, n):
            if A[i] > A[i - 1]:
                dp1[i] = dp2[i - 1] + 1
            if A[i] < A[i - 1]:
                dp2[i] = dp1[i - 1] + 1
        return max(max(dp1), max(dp2))
