"""
https://leetcode.com/problems/number-of-valid-subarrays/

For nums[i], we need to find next smaller element in nums[i+1:] and its index, let them be (v, j), then the number of valid subarrays using nums[i] as the leading element is (j - i).

We use a stack to keep track of (idx, value) pair of the element we have visited. When current visited value is smaller than the top value in the stack, we record it in the nextSmaller array. Keep popping until current value is larger than the value on top.

Each element is visited at most twice. Time complexity: O(N)
"""
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        nextSmaller = [len(nums)] * len(nums)
        for i, v in enumerate(nums):
            while stack and stack[-1][1] > v:
                nextSmaller[stack.pop()[0]] = i
            stack.append((i, v))
        return sum([v - i for i, v in enumerate(nextSmaller)])
