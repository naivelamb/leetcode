# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/kill-process/

Build tree, BFS
"""
import collections
class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        for i in range(len(pid)):
            graph[ppid[i]].append(pid[i])
        
        res = []
        queue = collections.deque([kill])
        while queue:
            node = queue.popleft()
            res.append(node)
            queue += graph[node]
        return res
