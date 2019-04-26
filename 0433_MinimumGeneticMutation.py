# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/minimum-genetic-mutation/

BFS
"""
import collections
class Solution:
    def minMutation(self, start, end, bank):
        diff = 0
        for i in range(len(start)):
            if start[i] != end[i]:
                diff += 1
        if diff  > len(bank):
            return -1
        bank = set(bank)
        seen = {start}
        deque = collections.deque([(start, 0)])
        while deque:
            curr, change = deque.popleft()
            if curr == end:
                return change
            for i in range(len(curr)):
                for ch in 'ACGT':
                    new_gene = curr[:i] + ch + curr[i+1:]
                    if new_gene not in seen and new_gene in bank:
                        bank.remove(new_gene)
                        deque.append((new_gene, change + 1))
                        seen.add(new_gene)
        return -1
