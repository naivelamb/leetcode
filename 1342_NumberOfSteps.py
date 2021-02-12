"""
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
Simulation.
"""
class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 1:
                num -= 1
            else:
                num /= 2
            steps += 1
        return steps