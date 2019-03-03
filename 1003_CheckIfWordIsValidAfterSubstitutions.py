# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

Use stack to remember the letters that have been seen. Pop out if the last 3 are
'abc'. At the end, check whether the stack is empty or not.
"""
class Solution:
    def isValid(self, S: str) -> bool:
        # 'abc' is valid
        stack = []
        for i in range(len(S)):
            stack.append(S[i])
            if len(stack) >= 3:
                if ''.join(stack[-3:]) == 'abc':
                    stack.pop()
                    stack.pop()
                    stack.pop()
        if stack:
            return False
        else:
            return True
