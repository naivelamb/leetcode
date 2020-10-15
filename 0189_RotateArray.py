"""
https://leetcode.com/problems/rotate-array/

View the nums with index difference of 'k' as a linked list. We shift all the nums in the linked list by one, until we found a cicle. Then we break and find next starting point of the linked list.

Time complexity: O(N)
Space complexity: O(1)
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k >= n or k == 0:
            return

        start, count = 0, 0
        while count < n:
            current = start
            prev = nums[start]

            while True:
                next = (current + k) % n
                temp = nums[next]
                numx[next] = prev
                prev = temp
                current = next
                count += 1

                if start == current: # circle
                    break
            start += 1
