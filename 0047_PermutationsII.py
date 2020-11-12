"""
https://leetcode.com/problems/permutations-ii/

#1 Backtracking. 

We stop recursion when we reaches desired depth, and the current sequence are not in answers. 

Else, we try every possible remain nums (track by index).

Hence, we need to pass two parameters to the recursion function:
1. curr -> record current sequence.
2. curr_idx -> record used indeces, this could be a set to improve efficient. 

Time complexity: O(n!)

#2 Improved version.
If we view the recursion tree, at the same level, we only have one node for one number, duplicate elements will belong to the same node. Hence we can sort the array in advance, and skip duplications in dfs. 

"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        def dfs(curr, curr_idx):
            if len(curr) == len(nums) and curr not in self.ans:
                self.ans.append(curr[:])
            for i in range(len(nums)):
                if i not in curr_idx:
                    curr_idx.add(i)
                    dfs(curr + [nums[i]], curr_idx)
                    curr_idx.remove(i)
        
        dfs([], set())
        return self.ans
    
    def permuteUnique_improved(self, nums):
        self.ans = []
        nums.sort()

        def dfs(nums, curr):
            if not nums:
                self.ans.append(curr[:])
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[:i] + nums[i+1:], curr + [nums[i]])
        
        dfs(nums, [])
        return self.ans