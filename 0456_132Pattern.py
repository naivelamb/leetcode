"""
https://leetcode.com/problems/132-pattern/

1. We need to know the prev_min.
If nums[i] > prev_min[i], we find a '13' pattern. Now we need to check whether we can find a j after i, that nums[j] > prev_min[i] and nums[j] < nums[i].

Time complexity: O(N)

2. Monotonic stack
We make sure the stack is monotonic decreasing. We visit the nums from right to left.
Given nums[i], we try to push it to the stack when:
1) The stack is empty.
2) nums[i] is smaller than stack[-1]
Otherwise we keep pop stack, and the last popped num is num2.
We do this until we find num1.

Time complexity: O(N)
"""
class Solution:
    def find132pattern(self, nums) -> bool:
        if len(nums) < 3:
            return False

        prev_min = [nums[0]]
        for i in range(1, len(nums)):
            prev_min.append(min(prev_min[i-1], nums[i]))
        stack = []
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > prev_min[j]:
                while stack and stack[-1] <= prev_min[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False

    def find132pattern_reverse(self, nums) -> bool:
        j, stack = float('-inf'), []
        for num in nums[::-1]:
            if num < j:
                return True
            while stack and stack[-1] < num:
                j = stack.pop()
            stack.append(num)
        return False
