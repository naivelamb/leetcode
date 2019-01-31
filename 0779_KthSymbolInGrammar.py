# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/k-th-symbol-in-grammar/

The Kth element from Nth row is coming from the (K + 1)//2 element in the (N-1)
row. 
Prev_element -> 0: candidates -> [0, 1]
Prev_element -> 1: candidates -> [1, 0]
k % 2 == 1 -> first candidate.
k % 2 == 0 -> second candidate.
Based on the above facts, we can use recursion to solve this problem.
"""
class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            return 0
        prevK = (K + 1) // 2
        prevN = self.kthGrammar(N - 1, prevK)
        nums = [[0, 1], [1, 0]]
        return nums[prevN][(K + 1) % 2]

