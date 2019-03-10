# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

Use dp to solve the problem. 
dp[i] stands for the minimum flips to make all A[:i] the same as A[0].

We can do this for 4 times:
    A, B
    B, A
    B[0] + A[1:], A[1] + B[1:]
    A[0] + B[1:], B[0] + A[1:]
Then compare the results.

Time complexity: O(n)
"""
class Solution:
    def minDominoRotations(self, A, B):
        def helper(A, B):
            # compute the minimum flip to make all A become A[0]
            dp, num = [0], A[0]
            for i in range(1, len(A)):
                if A[i] == num:
                    dp.append(dp[-1])
                elif B[i] == num:
                    dp.append(dp[-1] + 1)
                else:
                    return -1
            return dp[-1]
        
        ans1 = helper(A[:], B[:])
        ans2 = helper(B[:], A[:])
        ans3 = helper([B[0]] + A[1:], [A[0]] + B[1:])
        if ans3 != -1:
            ans3 += 1
        ans4 = helper([A[0]] + B[1:], [B[0]] + A[1:])
        if ans4 != -1:
            ans4 += 1
        res = [ans1, ans2, ans3, ans4]
        if all(x == -1 for x in res):
            return -1
        else:
            return min(x if x != -1 else float('inf') for x in res)
        