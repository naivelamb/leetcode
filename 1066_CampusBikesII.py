"""
https://leetcode.com/problems/campus-bikes-ii/

PQ to go through all possible combinations.

Time complexity: O(NM!)
"""
import heapq
from collections import defaultdict
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        pq = [(0, 0, '0'*len(bikes))]

        best = defaultdict(lambda: float('inf'))

        while pq:
            cost, i, bike_status = heapq.heappop(pq)
            if i == len(workers):
                return cost

            for j, b in enumerate(bikes):
                if bike_status[j] != '1':
                    new_cost = cost + dist(workers[i], b)
                    new_bike_status = bike_status[:j] + '1' + bike_status[j+1:]

                    if new_cost < best[(i+1, new_bike_status)]:
                        best[(i+1, new_bike_status)] = new_cost
                        heapq.heappush(pq, (new_cost, i+1, new_bike_status))

        return -1

sol = Solution()
workers = [[0,0],[2,1]]
bikes = [[1,2],[3,3]]
assert sol.assignBikes(workers, bikes) == 6
workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]
assert sol.assignBikes(workers, bikes) == 4
