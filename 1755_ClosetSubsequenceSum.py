"""
https://leetcode.com/problems/closest-subsequence-sum/

To get all possible subsequence sum, time complexity is O(2^n).
If we can get results half half, it will be O(2^(n/2))
Then we can go through one, binary search the other one. 

Time compleixty: O(2^(n/2) + 2^(n/2)n)

"""
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def dfs(i, curr, arr, sums):
            if i == len(arr):
                sums.add(curr)
                return
            dfs(i + 1, curr, arr, sums)
            dfs(i + 1, curr + arr[i], arr, sums)
        
        sums1, sums2 = set(), set()
        dfs(0, 0, nums[:len(nums)//2], sums1)
        dfs(0, 0, nums[len(nums)//2:], sums2)

        s2 = sorted(sums2)
        ans = float('inf')

        for s in sums1:
            target = goal - s
            i2 = bisect_left(s2, target)
            if i2 < len(s2):
                ans = min(ans, abs(target - s2[i2]))
            if i2 > 0:
                ans = min(ans, abs(target - s2[i2 - 1]))
        return ans