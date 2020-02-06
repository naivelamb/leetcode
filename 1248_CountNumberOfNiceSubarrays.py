"""
https://leetcode.com/problems/count-number-of-nice-subarrays/

Prefix sum + hashmap

Let a_i be the number of odd number in subarray nums[0:i+1]
To get the number of the nice subarrays ending with i, we need to look forward, find the number of subarrays with odd number (k - a_i). This information can be stored in a hashmap.

Time complexity: O(N)
"""

class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        ref = {0: 1}
        cnt = ans = 0
        for i, num in enumerate(nums):
            if num % 2 == 1:
                cnt += 1

            ans += ref.get(cnt - k, 0)
            ref[cnt] = ref.get(cnt, 0) + 1

        return ans

sol = Solution()

nums = [1,1,2,1,1]
k = 3
assert sol.numberOfSubarrays(nums, k) == 2

nums = [2,4,6]
k = 1
assert sol.numberOfSubarrays(nums, k) == 0

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
assert sol.numberOfSubarrays(nums, k) == 16
