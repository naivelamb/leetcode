"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/

Use stack to record the numbers, when coming to operators, pop last two, compute the results and push back. 

Time complexity: O(N)
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            try:
                stack.append(int(t))
            except:
                b, a = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(a+b)
                elif t == '-':
                    stack.append(a-b)
                elif t == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack[-1]