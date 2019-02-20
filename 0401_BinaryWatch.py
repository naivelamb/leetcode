# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/binary-watch/

DFS + backtracking
"""
class Solution:
    def readBinaryWatch(self, num: 'int') -> 'List[str]':
        nums = [1, 2, 4, 8, 16, 32, 100, 200, 400, 800]
        res = []
        
        def dfs(n, idx, path):
            if n == num:
                hours, mins = divmod(path, 100)
                if hours > 11 or mins > 59:
                    return
                res.append('%d:%02d'.format(hours, mins))
                return
            for i in range(idx, len(nums)):
                dfs(n + 1, i + 1, path + nums[i])
        
        dfs(0, 0, 0)
        return res
