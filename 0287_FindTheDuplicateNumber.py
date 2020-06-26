"""
https://leetcode.com/problems/find-the-duplicate-number/

All numbers are in the range of [1, n], we can view the number as index, it becomes a linked list. Duplicate means there are circle in the linked list.

Slow & fast pointer.

Time Complexity: O(N)
"""
class Solution:
    def findDuplicate(self, nums) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
