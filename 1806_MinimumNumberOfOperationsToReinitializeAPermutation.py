"""
https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

Simulation. To make sure we return back to initial permutation, just need to check position-1.

Time complexity: O(N)
"""
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        ans = 0
        v = [x for x in range(n)]
        while True:
            tmp = v.copy()
            for i in range(n):
                if i % 2 == 0:
                    tmp[i] = v[i//2]
                else:
                    tmp[i] = v[(n + i - 1)//2]
            ans += 1
            if tmp[1] == 1:
                return ans
            else:
                v = tmp