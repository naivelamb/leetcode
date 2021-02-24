"""
https://leetcode.com/problems/score-of-parentheses/

Use a stack to manage data. 
When we see '(', append to stack.
When we see ')', need to check prevous element.
If previous is a number, we need to stack[-1] to current value. 
Else, we need to check if current value is 0 or not.
If it is 0, we need to append 1. 
Else, we need to append(2 * current_value).
At the end, sum the stack.

Time complexity: O(N)
"""
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for ch in S:
            if ch == '(':
                stack.append('(')
            else:
                curr = 0
                while stack[-1] != '(':
                    curr += stack.pop()
                stack.pop()
                stack.append(max(1, curr * 2))
        return sum(stack)        