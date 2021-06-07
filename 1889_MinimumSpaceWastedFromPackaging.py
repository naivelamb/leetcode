"""
https://leetcode.com/problems/minimum-space-wasted-from-packaging/

When using boxes, need to be greedy, use the box to package as many packages as possible. 

If packages are sorted, then we can use binary search to find number of packages that can be covered by the given box. 
==> need sorted packages and sorted boxes for each supplier. 

Time complexity: O(mlogm + nklog(mk))

m = len(packages), n = len(boxes), k => max(len(box) for box in boxes)
"""
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        p_sum = [0]
        for x in packages:
            p_sum.append(p_sum[-1] + x)
        ans = float('inf')
        MOD = 10**9 + 7
        # nlogn
        
        for bs in boxes: #m
            bs.sort() #klogk
            tmp, p_i = 0, 0
            if bs[-1] < packages[-1]:
                continue
            for s in bs: #k
                idx = bisect.bisect_right(packages, s) #logn
                tmp += s * (idx - p_i) - p_sum[idx] + p_sum[p_i]
                p_i = idx
            ans = min(ans, tmp)
        # nlogn + m(klogk + klogn)
        if ans == float('inf'):
            return -1
        return ans % MOD