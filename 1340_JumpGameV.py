"""
https://leetcode.com/problems/jump-game-v/
dp[i] -> the maximum jumps we can do starting from index i.
dp[i] = 1 + max(dp[j]), where j is all the indices we can visited from i.

Time complexity: O(nd)
"""
class Solution:
    def maxJumps(self, arr, d: int) -> int:
        n = len(arr)
        res = [0] * n

        def dp(i):
            if res[i]: return res[i]
            res[i] = 1
            for di in [-1, 1]:
                for j in range(i+di, i + d*di + di, di):
                    if not (0 <= j < n and arr[j] < arr[i]):
                        break
                    res[i] = max(res[i], 1 + dp(j))
            return res[i]
        return max(map(dp, range(n)))

sol = Solution()
assert sol.maxJumps([6,4,14,6,8,13,9,7,10,6,12], 2) == 4
assert sol.maxJumps([3,3,3,3,3], 2) == 3
assert sol.maxJumps([7,6,5,4,3,2,1], 1) == 7
