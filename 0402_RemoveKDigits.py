"""
https://leetcode.com/problems/remove-k-digits/

Go through the number for left to right. Use stack to record the visited number.
If current visited digit is smaller than the last element in the stack, stack.pop(). Keep doing this until the digit == stack[-1] or stack is empty. Append the digit to stack.
After doing this, if k != 0, keep poping stack until k == 0. Then remove leading '0' and return final answer.

Time complexity: O(2n), n = len(nums), since each element is visited at most twice. 
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'
        stack = []
        for ch in num:
            while k > 0 and len(stack) > 0 and int(stack[-1]) > int(ch):
                stack.pop()
                k -= 1
            stack.append(ch)

        while k > 0:
            stack.pop()
            k -= 1
        for i in range(len(stack)):
            if stack[i] != '0':
                break
        stack = stack[i:]

        return ''.join(stack) if stack else '0'

sol = Solution()
assert sol.removeKdigits("1432219", 3) == "1219"
assert sol.removeKdigits("10200", 1) == "200"
assert sol.removeKdigits("10", 2) == "0"
