# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

Use a stack to remember the preocessed string.
Time compelxity: O(n)
"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if stack[-1] == c:
                    stack.pop()
                else:
                    stack.append(c)
        return ''.join(stack)

