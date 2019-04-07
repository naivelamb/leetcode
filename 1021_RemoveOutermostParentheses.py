# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/remove-outermost-parentheses/

Find segment, remove the most outer parentheses

Time complexity: O(n), n -> len(S)
"""

class Solution:
    def removeOuterParentheses(self, S: str) -> str:   
        res = []
        start, curr, balance = 0, 1, 1
        while curr < len(S):
            if S[curr] == '(':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                res.append(S[start+1:curr ])
                start = curr + 1
            curr += 1
        return ''.join(res)
    
s = Solution()
print(s.removeOuterParentheses('(()())(())'))