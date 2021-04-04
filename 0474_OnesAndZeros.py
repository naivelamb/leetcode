"""
https://leetcode.com/problems/ones-and-zeroes/

dp(i, m, n), largest subset for nums[i:]
For every index, we can pick or not pick. 

If we pick, ans = 1 + dp(i+1, m-a, n-b), where a = strs[i].count('0'), b = strs[i].count('1')
If we don't pick, ans = dp(i+1, m, n)

time complexity: O(lmn)
"""
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr = [[s.count('0'), s.count('1')] for s in strs]

        @lru_cache(None)
        def dp(i, m, n):
            if i == len(strs):
                return 0
            
            ans = dp(i + 1, m, n)
            if m >= arr[i][0] and n >= arr[i][1]:
                ans = max(ans, dp(i+1, m - arr[i][0], n - arr[i][1]) + 1)
            return ans
        return dp(0, m, n)