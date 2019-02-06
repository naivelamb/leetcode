# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/factor-combinations/

Try to decompose the largest number. 
[12] => [2, 6] or [3, 4] => [2, 2, 3]. 
The divider never decrease, this make sure we won't duplicate. 
"""
class Solution:
    def getFactors(self, n: 'int') -> 'List[List[int]]':
        def dfs(cur, i):
            # cur -> list of current factors
            # i -> current divider
            # try to find the next smallest divider, create new cur
            num = cur.pop()
            while i**2 <= num:
                div = num // i
                if num % i == 0:
                    res.append(cur + [i, div])
                    dfs(cur + [i, div], i)
                i += 1
        res = []
        dfs([n], 2)
        return res
    
s = Solution()
print(s.getFactors(12))
