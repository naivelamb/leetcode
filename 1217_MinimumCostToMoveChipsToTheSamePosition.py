"""
https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

Count the number of chips in odd & even positions respectively, answer is the minimum one. 

Time complexity: O(N)
"""
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        ref = collections.defaultdict(int)
        for p in position:
            if p % 2 == 0:
                ref[0] += 1
            else:
                ref[1] += 1
        return min(ref[0], ref[1])