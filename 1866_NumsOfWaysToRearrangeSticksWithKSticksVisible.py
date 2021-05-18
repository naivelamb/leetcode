"""
https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

let dp(n, k) be the number of arrange for n numbers that see k sticks. 

If nums[n-1] is the largest one, then there are dp(n-1, k-1) ways of arrangements.
Else, there are (n-1) * dp(n-1, k) ways of arrangements. 

Time complexity: O(NK)
"""
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def fn(n, k):
            if n == k: return 1
            if k == 0: return 0
            return ((n-1) * fn(n-1, k) + fn(n-1, k-1)) % MOD

        return fn(n, k) % MOD

s = Solution()
n = 13
k = 11
print(s.rearrangeSticks(n, k))