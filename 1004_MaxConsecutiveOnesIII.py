# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/max-consecutive-ones-iii/

Similar to 487. Use two pointers, make sure # of 0s within the window <= K

Time Complexity: O(n), each element is scaned for at most twice.
"""
class Solution:
    def longestOnes(self, A, K):
        if not A:
            return 0
        slow = fast = cnt = ans = 0
        while fast < len(A):
            if A[fast] == 0:
                cnt += 1
            fast += 1
            while cnt > K:
                if A[slow] == 0:
                    cnt -= 1
                slow += 1
            ans = max(ans, fast - slow)
        return ans

