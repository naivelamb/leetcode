"""
https://leetcode.com/problems/next-permutation/

We first try to find the longest suffix that is non-increasing. This suffix would be at its highest permutation, so we cannot make a next permutation by modify it. We need to modify some elements to the left of it. 

Then we take the element immediately to the left of the suffix, and call it pivot. We are going to swap it with its successor in the suffix. If no succesor, we will swap it with the last element in the suffix. 

At last we just need to reverse the suffix. 

In summary, 
1. find longest non-increasing suffix (from right)
2. identify pivoit
3. find rightmost successor to the pivot in the suffix
4. swap with pivot
5. reverse the suffix
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        pivot = n - 1
        while pivot >= 0:
            if nums[pivot - 1] < nums[pivot]:
                break
            pivot -= 1
        pivot -= 1
        if pivot == -1:
            nums.reverse()
            return
        
        swap = pivot + 1
        while swap < n:
            if nums[swap] <= nums[pivot]:
                break
            swap += 1
        swap -= 1

        nums[swap], nums[pivot] = nums[pivot], nums[swap]
        nums[pivot + 1:] = nums[pivot + 1:][::-1]
        return 