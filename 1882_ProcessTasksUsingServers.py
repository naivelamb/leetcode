"""
https://leetcode.com/problems/process-tasks-using-servers/

2 simulation min heap. 
heap1 record the current available servers. 
heap2 record the current unavailable servers.

time complexity: O(mlogn), m = len(tasks), n = len(servers)
"""
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = [-1] * len(tasks)
        h1 = [[weight, i] for i, weight in enumerate(servers)]
        h2 = []
        heapq.heapify(h1)
        t = 0
        for j, task in enumerate(tasks):
            t = max(t, j)
            if not h1:
                t = h2[0][0]
            while h2 and t >= h2[0][0]:
                t1, w, idx = heapq.heappop(h2)
                heapq.heappush(h1, [w, idx])
            
            w, idx = heapq.heappop(h1)
            heapq.heappush(h2, (t + task, w, idx))
            res[j] = idx
        return res
        
        