"""
https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

Record number of balls in each box, return the maximum one.

Time complexity: O(N)
"""
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ans, cnt = 0, {}
        for x in range(lowLimit, highLimit + 1):
            v = 0
            while x != 0:
                v += x%10
                x //= 10
            cnt[v] = cnt.get(v, 0) + 1
            ans = max(ans, cnt[v])
        return ans