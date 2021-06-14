"""
https://leetcode.com/problems/maximum-units-on-a-truck/

Greedy, always try to put the largest boxes. 

Time complexity: O(nlogn), n = len(boxTypes)
"""
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        ans = 0
        i = 0
        while truckSize and i < len(boxTypes):
            n, s = boxTypes[i]
            n = min(truckSize, n)
            ans += n * s
            truckSize -= n
            i += 1

        return ans