"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Go from left to right, remove open ')'. Then go from right to left, remove open '('

Time complexity: O(2N)
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = []
        stack = []
        for ch in s:
            if ch == '(':
                ans.append(ch)
                stack.append('(')
            elif ch == ')':
                if stack:
                    ans.append(ch)
                    stack.pop()
            else:
                ans.append(ch)

        stack = []
        tmp_ans = ans.copy()
        ans = []
        for i in range(len(tmp_ans) - 1, -1, -1):
            ch = tmp_ans[i]
            if ch == ')':
                ans.append(ch)
                stack.append('')
            elif ch == '(':
                if stack:
                    ans.append(ch)
                    stack.pop()
            else:
                ans.append(ch)
        return ''.join(ans)[::-1]        