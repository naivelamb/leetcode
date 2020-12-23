"""
https://leetcode.com/problems/next-greater-element-iii/

Go from the back, find the longest sequence that is descending order. 
Locate the last asending position, from the end find the first one that are larger than this number, switch them. 
Then just reverse the "descending" part. 

Time complexity: O(m), where m = # of digits of n
"""
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(map(int, list(str(n))))
        i = j = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0: # nums are maximum
            return -1
        k = i - 1
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        res = 0
        for x in nums:
            res = res * 10 + x
        if res > 2**31 - 1:
            return -1
        else:
            return res   