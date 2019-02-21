# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/valid-parentheses/

Stack to store unused 'left', scan from the left
At the end, make sure all element in stack is used.
"""
class Solution:
    def isValid(self, s: 'str') -> 'bool':
        ref = {')': '(',
               ']': '[',
               '}': '{',
               }
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if stack[-1] == ref[c]:
                    stack.pop()
                else:
                    return False
        return not stack
