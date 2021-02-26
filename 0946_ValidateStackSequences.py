"""
https://leetcode.com/problems/validate-stack-sequences/

Simulate, push element in pushed to a stack one by one, when we see the last element is in popped, pop it. If at the end, popped is not empty return False, else True.

Time complexity: O(N)
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for x in pushed:
            stack.append(x)
            while i < len(popped) and stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        if not stack:
            return True
        return False