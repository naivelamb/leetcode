# -*- coding: utf-8 -*-
"""
This FB interview version, which only requres to return one valid string.

We first compute the number of left/right parentheses -> l, r
We scan from left to right, if we see an unneeded right, we remove.
Then we scan from right to left, if we seen an unneeded left, we remove. 
"""
import collections
class Solution:
    def removeInvalidParentheses(self, s: 'str') -> 'List[str]':
        tmp = []
        l = 0
        for ch in s:
            if ch == '(':
                l += 1
                tmp.append(ch)
            elif ch == ')':
                if l > 0:
                    l -= 1
                    tmp.append(ch)
            else:
                tmp.append(ch)
        r, res = 0, []
        for ch in tmp[::-1]:
            if ch == ')':
                r += 1
                res.append(ch)
            elif ch == '(':
                if r > 0:
                    r -= 1
                    res.append(ch)
            else:
                res.append(ch)
        return ''.join(res[::-1])
        
    def isValid(self, s):
        # compute the '(' and ')' that need to be removed
        l, r = 0, 0
        for ch in s:
            if ch == '(':
                l += 1
            if ch == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1
        return l == 0 and r == 0
    
s = Solution()
a = '()())()'
print(s.removeInvalidParentheses(a), s.isValid(s.removeInvalidParentheses(a)))
a = ')('
print(s.removeInvalidParentheses(a), s.isValid(s.removeInvalidParentheses(a)))
a = '()'
print(s.removeInvalidParentheses(a), s.isValid(s.removeInvalidParentheses(a)))
a = '(a)'
print(s.removeInvalidParentheses(a), s.isValid(s.removeInvalidParentheses(a)))
a = '(a)()))(()'
print(s.removeInvalidParentheses(a), s.isValid(s.removeInvalidParentheses(a)))
