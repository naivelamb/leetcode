"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/

Count, then find pairs. Be careful when 2*x == k

Time complexity: O(N)
"""
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = collections.Counter(nums)
        ans = 0
        for v in cnt:
            if k >= v:
                op = min(cnt[v], cnt[k-v])
                if v == k - v:
                    op //= 2
                if op > 0: #update count
                    cnt[v] = max(0, cnt[v] - op) 
                    cnt[k-v] = max(0, cnt[k-v] - op)
                ans += op
        return ans   