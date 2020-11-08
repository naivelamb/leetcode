"""
https://leetcode.com/problems/get-maximum-in-generated-array/

Simulation, time complexity: O(n)

"""
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        res = [0, 1]
        ans = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                val = res[i//2]
            else:
                val = res[i//2] + res[i//2 + 1]
            res.append(val)
            ans = max(ans, val)
        return ans