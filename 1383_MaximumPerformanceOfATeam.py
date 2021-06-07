"""
https://leetcode.com/problems/maximum-performance-of-a-team/

If we sort the engineers by efficiency, everytime we add a new engineer, we increase speed, but decrease efficiency. 

We use maintain a PQ of length K, if the size exceeds, we remove the one with smallest speed. 

Time complexity: O(NlogN + NlogK)
"""
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        h = []
        res = sSum = 0
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(h, s)
            sSum += s
            if len(h) > k:
                sSum -= heapq.heappop(h)
            res = max(res, sSum * e)
        return res % (10**9 + 7)