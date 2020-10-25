"""
https://leetcode.com/problems/slowest-key/

Compute the duration time and record the longest one.

Time complexity: O(N)
"""
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans = keysPressed[0]
        time = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            t = releaseTimes[i] - releaseTimes[i-1]
            if t > time:
                time = t
                ans = keysPressed[i]
            elif t == time:
                ans = max(ans, keysPressed[i])
            else:
                pass
        return ans