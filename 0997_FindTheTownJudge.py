# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 23:13:40 2019

Scan the trust, for each people, record:
1. # of people he trust
2. # of people trusted him

Time Comeplexity: O(n)
"""

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        cnt = [[0, 0] for _ in range(N + 1)]
        for a, b in trust:
            cnt[a][0] += 1
            cnt[b][1] += 1
        
        for i in range(1, len(cnt)):
            if cnt[i][0] == 0 and cnt[i][1] == N -1:
                return i
        return -1