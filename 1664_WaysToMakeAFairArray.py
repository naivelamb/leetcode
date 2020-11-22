"""
https://leetcode.com/problems/ways-to-make-a-fair-array/

DP. 
odd_sum[i] == odd_sum of nums[:i+1]
even_sum[i] == even_sum of nums[:i+1]

After remove i, then even_sum after i becomes odd_sum, vice versa. 

Time complexity: O(N)
"""
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd_sum, even_sum = [0], [nums[0]]
        for i in range(1, len(nums)):
            if i % 2 != 0:
                odd_sum.append(odd_sum[-1] + nums[i])
                even_sum.append(even_sum[-1])
            else:
                odd_sum.append(odd_sum[-1])
                even_sum.append(even_sum[-1]+ nums[i])  
        
        ans, total = 0, sum(nums)
        for i in range(len(nums)):
            if (total - nums[i]) % 2 != 0:
                continue
            after_even = even_sum[-1] - even_sum[i]
            after_odd = odd_sum[-1] - odd_sum[i]
            pre_even = even_sum[i] - nums[i] * (i % 2 == 0)
            pre_odd = odd_sum[i] - nums[i] * (i % 2 != 0)
            if after_even + pre_odd == after_odd + pre_even:
                ans += 1
        return ans