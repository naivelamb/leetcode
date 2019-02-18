# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/additive-number

If we know v1 and v2, then we can check whether it is satisfied.
We need to try all possible v1 and v2 combinations. => nested for loop. 
Check can be done recursively.  
"""
class Solution:
    def isAdditiveNumber(self, num: 'str') -> 'bool':
        def dfs(v1, v2, num):
            if not num:
                return True
            sums = str(int(v1) + int(v2))
            ls, ln = len(sums), len(num)
            if ls > ln or (len(v1) > 1 and v1.startswith('0')) or (len(v2) > 1 and v2.startswith('0')) or sums != num[:ls]:
                return False
            else:
                return dfs(v2, sums, num[ls:])
        for i in range(1, len(num) - 1):
            for j in range(i + 1, len(num)):
                if dfs(num[:i], num[i:j], num[j:]):
                    return True
        return False
        
s = Solution()
print(s.isAdditiveNumber('112358'))
print(s.isAdditiveNumber('199100199'))