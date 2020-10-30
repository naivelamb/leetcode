"""
https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

Record pre_sum. 
If pre_sum[i] is odd, we need to find number of even pre_sum[j] for j < i, since sum(j, i+1) -> odd;
If pre_sum[i] is even, we need to find number of odd pre_sum[j] for j < i, since sum(j, i+1) -> odd.

Time complexity: O(N)
"""
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        pre_sum = arr[0]
        pre_state = arr[0] % 2 # pre odd sum
        ans = pre_state
        for i in range(1, len(arr)):
            pre_sum += arr[i]
            pre_state += pre_sum % 2
            if pre_sum % 2 == 1:
                ans += (i + 1 - pre_state + 1)
            else:
                ans += pre_state
        return ans % (10**9 + 7)