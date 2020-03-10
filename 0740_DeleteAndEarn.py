"""
https://leetcode.com/problems/delete-and-earn/

We can delete all same numbers together. Each number has two option: keep or remove.
Let cnt[num] be the number of counts for num.
keep[i] -> maximum score if we keep i; -> this is equivilant to remove i due to we remove i or (i+1)
remove[i] -> maximum score if we remove i;

remove[i] = keep[i-1] + cnt[i] * i
keep[i] = max(remove[i-1], keep[i-1])

Time complexity: O(m + n)
n = len(nums)
m = max(nums) - min(nums)
"""
class Solution:
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        cnt = {}
        n_min, n_max = float('inf'), float('-inf')
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
            n_min = min(n, n_min)
            n_max = max(n, n_max)

        prev_remove, prev_keep, ans = 0, 0, 0
        for i in range(n_min, n_max + 1):
            curr_remove = prev_keep + cnt.get(i, 0) * i
            curr_keep = max(prev_keep, prev_remove)
            prev_remove, prev_keep = curr_remove, curr_keep
            ans = max(curr_remove, curr_keep)
        return ans

sol = Solution()
assert sol.deleteAndEarn([3,4,2]) == 6
assert sol.deleteAndEarn([2,2,3,3,3,4]) == 9
