# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

Use stack to remember the letters that have been seen. Pop out if the last 3 are
'abc'. At the end, check whether the stack is empty or not.

Time Complexity: O(n)
"""
class Solution:
    def isValid(self, S: str) -> bool:
        # 'abc' is valid
        stack = []
        for ch in S:
            if ch == 'c':
                if stack[-2:] == ['a', 'b']:
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        if stack:
            return False
        else:
            return True
