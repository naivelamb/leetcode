"""
https://leetcode.com/problems/jump-game-vi/

dp[i] => max score to reach position-i 
dp[i] = nums[i] + min(dp[j]) for j in [j-k, j-1].
Time complexity: O(nk)

Let's maintain a sliding window, such that:
(1) its size is <= k
(2) its first element is the largest one. 

Time complexity: O(n)
"""
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # O(nk)
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = nums[0]
        for i in range(1, n):
            l = max(0, i-k)
            dp[i] = nums[i] + max(dp[l:i])
        return dp[-1]

    def maxResult_On(self, nums: List[int], k: int) -> int:
        # O(n)
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = nums[0]
        d = deque([(nums[0], 0)])
        for i in range(1, n):
            dp[i] = nums[i] + d[0][0]
            while d and d[-1][0] < dp[i]:
                d.pop()
            d.append((dp[i], i))
            if i - k == dp[0][1]:
                d.popleft()
        return dp[-1]        