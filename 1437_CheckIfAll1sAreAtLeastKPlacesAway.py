"""
https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

Use a stack to store the position of last 1, compute and check. 

Time complexity: O(N)
"""

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        stack = []
        for i, n in enumerate(nums):
            if n == 1:
                if stack and i - stack[-1] <= k:
                    return False
                stack.append(i)
        return True