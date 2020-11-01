"""
https://leetcode.com/problems/kth-smallest-instructions/

Given the destination, we know the number of "H" and "V" we need to arrange. 

If we start with "H", we know how many combinations we could have, vice versa. 

So we can try this until we find k. 

Time complexity: O(m + n)
"""
import math
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        V, H = destination
        n = H + V
        def helper(n, H):
            return math.comb(n, H)
        
        ans = ""
        while len(ans) != n:
            if H == 0 and V == 0:
                break
            elif H == 0 or V == 0:
                if H == 0:
                    ans += "V"
                    V -= 1
                elif V == 0:
                    ans += "H"
                    H -= 1
            else:
                if helper(H + V - 1, H - 1) >= k:
                    ans += "H"
                    H -= 1
                else:
                    ans += "V"
                    k -= helper(H + V - 1, H - 1)
                    V -= 1
        return ans
