"""
https://leetcode.com/problems/first-missing-positive/

For any array whose length is l, the 1st missing positive must be in the range [1, ..., l+1], so we only need to care those elements in this range.

We can use the array index as the hash to restore the frequency of each element within the range [1, ..., l+1].

Time Complexity: O(N)

"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        # remove useless elements
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        # record frequency
        for i in range(n):
            nums[nums[i] % n] += n
        for i in range(1, n):
            if nums[i] // n == 0:
                return i
        return n
