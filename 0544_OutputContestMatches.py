# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/output-contest-matches/

Each pair, sum of rank == n + 1
The result of n can be derived from the pairs for n//2. 
Time Complexity: O(nlogn)
"""
class Solution:
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = [str(x) for x in range(1, n+1)]
        while n > 1:
            seq = ['(' + seq[i] + ',' + seq[n-1-i] + ')' for i in range(n//2)]
            n //= 2
        return seq[0]
