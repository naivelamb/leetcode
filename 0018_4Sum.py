"""
https://leetcode.com/problems/4sum/

Sort, fix two starting point, the use two pointers to go through the rest.

Time complexity: O(N^3)
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if len(nums) < 4:
            return []
        res = set()

        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                k, l = j + 1, len(nums) - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total > target:
                        l -= 1
                    elif total < target:
                        k += 1
                    else:
                        res.add(([nums[i], nums[j], nums[k], nums[l]]))
                        k += 1
                        l -= 1
        ans = [list(x) for x in res]
        return ans

    def fourSum_general(self, nums, target):
        nums.sort()
        self.ans = []

        def findNSum(nums, target, N, chosen):
            if len(nums) < N or N < 2 or nums[-1] * N < target or nums[0] * N > target:
                return 
            
            if N == 2: # 2Sum
                l, r = 0, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == target:
                        self.ans.append(chosen + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        l += 1
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    findNSum(nums[i+1:], target-nums[i], N-1, chosen + [nums[i]])
        
        findNSum(nums, target, 4, [])
        return self.ans