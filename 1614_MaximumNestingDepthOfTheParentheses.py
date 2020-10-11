"""
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

Use a stack to record "(" and depth += 1, pop "(" from the stack when seen ")" and depth -= 1.

Time complexity: O(N)
"""
class Solution:
    def maxDepth(self, s: str) -> int:
        ans, curr = 0, 0
        stack = []
        for ch in s:
            if ch == '(':
                curr += 1
                stack.append(ch)
            if ch == ')':
                curr -= 1
                stack.pop()
            ans = max(ans, curr)
        return ans
