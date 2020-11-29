"""
https://leetcode.com/problems/find-the-most-competitive-subsequence/

Essential we are maintian a monotoic increasing stack. 
When we see a number smaller then the last element in the stack, and there are enough remaining nums to make stack to length k, we can pop the stack. 

Time complexity: O(N)
"""
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i, a in enumerate(nums):
            while stack and stack[-1] > a and len(stack) - 1 + len(nums) - i >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(a)
        return stack
