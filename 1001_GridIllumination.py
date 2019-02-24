# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/grid-illumination/

If diagonal is from left-down to right-up, => diagonal
then (i + j) is a constant.
If diagonal is from left-top to right-down, => right diagonal
then (i - j) is a constant. 

Use 4 dict to record row, column, diagonal and right diagonal. Check illuminated
can be done in O(1). 

Time Complexity: O(m + n)
m -> len(lamps)
n -> len(queries)
"""
import collections
class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        diags = collections.defaultdict(set)
        rdiags = collections.defaultdict(set)
        
        for i, j in lamps:
            rows[i].add((i, j))
            cols[j].add((i, j))
            diags[i + j].add((i, j))
            rdiags[i - j].add((i, j))
        
        ans = [0] * len(queries)
        for k, (x, y) in enumerate(queries):
            qrow, qcol, qdiag, qrdiag = rows[x], cols[y], diags[x + y], rdiags[x - y]
            if any([qrow, qcol, qdiag, qrdiag]):
                ans[k] = 1
            
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    qrow, qcol, qdiag, qrdiag = rows[i], cols[j], diags[i + j], rdiags[i - j]
                    for s in [qrow, qcol, qdiag, qrdiag]:
                        if s:
                            s.discard((i, j))
        return ans
        