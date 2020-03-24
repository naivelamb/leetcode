"""
https://leetcode.com/problems/jump-game-v/
"""
class Solution:
    def maxJumps(self, arr, d: int) -> int:
        return 0

sol = Solution()
assert sol.maxJumps([6,4,14,6,8,13,9,7,10,6,12], 2) == 4
assert sol.maxJumps([3,3,3,3,3], 2) == 3
assert sol.maxJumps([7,6,5,4,3,2,1], 1) == 7
