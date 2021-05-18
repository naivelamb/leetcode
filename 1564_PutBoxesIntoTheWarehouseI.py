"""
https://leetcode.com/problems/put-boxes-into-the-warehouse-i/

Greedy. Sort boxes, always push the lowest box first.

Time complexity: O(nlogn + m)
"""
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        pre_min = [warehouse[0]]
        for x in warehouse[1:]:
            pre_min.append(min(x, pre_min[-1]))
        boxes.sort()
        ans, i, j = 0, len(warehouse) - 1, 0
        while j < len(boxes) and i >= 0:
            if boxes[j] <= pre_min[i]:
                j += 1
                ans += 1
            i -= 1
        return ans