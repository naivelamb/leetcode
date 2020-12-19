"""
https://leetcode.com/problems/4sum-ii/

Store count of (a+b) into a hash table. For all (c+d) find the count of -(c+d).

Time complexity: O(A*B + C*D)
"""

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        cnt = {}
        for a in A:
            for b in B:
                cnt[a+b] = cnt.get(a+b, 0) + 1
        ans = 0
        for c in C:
            for d in D:
                ans += cnt.get(-c-d, 0)
        
        return ans