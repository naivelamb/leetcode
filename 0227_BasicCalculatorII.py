"""
https://leetcode.com/problems/basic-calculator-ii/

Use a stack to store ops, another stack to store nums. 
When we see nums, we need to check the last op, if it is '*/', we need to do the computation. 
At the end, ops stack only have '+-'. We can easily compute the final value. 

Time complexity: O(N)
"""
class Solution:
    def calculate(self, s: str) -> int:
        ops, nums = [], []
        i = 0
        while i < len(s):
            if s[i] == " ":
                pass
            elif s[i] in "+-*/":
                ops.append(s[i])
            else: # digit
                num = int(s[i])
                while i + 1 < len(s) and s[i+1].isdigit():
                    num = num * 10 + int(s[i+1])
                    i += 1
                if ops and ops[-1] in "*/":
                    op = ops.pop()
                    num_prev = nums.pop()
                    if op == "*":
                        num = num * num_prev
                    else:
                        num = int(num_prev / num)
                nums.append(num)
            i += 1
        
        ans = nums[0]
        for i in range(len(ops)):
            if ops[i] == '+':
                ans += nums[i+1]
            else:
                ans -= nums[i+1]
        return ans