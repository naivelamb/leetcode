"""
https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

We will start with the job has maximum required energy, and minimum spend energy. 

Heap. 

Time complexity: O(NlogN)
"""
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        task_order = [[y - x, y, x] for x, y in tasks]
        heapq.heapify(task_order)

        ans = 0
        while task_order:
            _, y, x = heapq.heappop(task_order)
            ans += x
            ans = max(ans, y)
        return ans