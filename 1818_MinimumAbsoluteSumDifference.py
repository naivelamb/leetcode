"""
https://leetcode.com/problems/minimum-absolute-sum-difference/

First compute the abs diff sum. Then for each (a, b) pair, we need to find the nearest v in nums1 ==> binary serach. 

Time comlexity: O(nlogn)
"""
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10 ** 9 + 7
        cnt = {}
        ans = 0
        for a, b in zip(nums1, nums2):
            ans += abs(a - b)
            cnt[a] = cnt.get(a, 0) + 1
        
        cands = sorted(list(cnt.keys()))
        
        curr = ans
        for i, a in enumerate(nums1):
            b = nums2[i]
            if a == b:
                continue
            idx = bisect.bisect_left(cands, b)
            cand = []
            if idx - 1 >= 0:
                cand.append(abs(cands[idx - 1] - b)) 
            if 0 <= idx < len(cands):
                cand.append(abs(cands[idx] - b))
            if 0 <= idx + 1 < len(cands):
                cand.append(abs(cands[idx + 1] - b))
            if cand:
                curr = min(curr, ans - abs(a - b) + min(cand))
        return curr % MOD                
            