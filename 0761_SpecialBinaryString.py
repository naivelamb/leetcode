# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/special-binary-string/

If we know two consecutive non-empty speical substratings, s1 and s2, the lexi-
-cographically largest string is ''.join(sorted(s1, s2)[::-1]).

If we have a special string like 1M0, them M must be another speical string, 
the largest string after swap would be '1' + makeLargestSpecial(M) + '0'. 

Therefore we build a recursion path. We first split the string to the form 1M0
as many as possible, then make all the substring largest. At last, we sort them
and assemble. 

Time complexity: O(n^2)
"""
class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        count, curr = 0, 0
        res = []
        for i, ch in enumerate(S):
            count = count + 1 if ch == '1' else count - 1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(S[curr+1: i]) + '0')
                curr = i + 1
        return ''.join(sorted(res)[::-1])