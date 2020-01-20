# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/campus-bikes/

m = len(workers), n = len(bikes)
First loop over all woker-bike pairs, compute the distance and store information
into a dists array.

dists[i]: the (distance, worker_idx, bike_idx) for worker_i.
dists[i] need to be sort, so we will heapify it.

This process takes O(mn)

Next we need to search from the shortest distance, which is
[dist[0] for dist in dists] -> this need to be heapify.

If a (worker, bike) pair has been used, we need to get next candidate, dists[worker].

 
"""
import heapq
class Solution:
    def assignBikes(self, workers, bikes):
        dists = [] #(distance, worker_idx, bike_idx)
        for i, worker in enumerate(workers):
            tmp = []
            for j, bike in enumerate(bikes):
                tmp.append((self.get_distance(bike, worker), i, j))
            dists.append(tmp)
            heapq.heapify(dists[i])

        heap = [dist[0] for dist in dists]
        heapq.heapify(heap)
        res = [0] * len(workers)
        count = 0
        used_worker, used_bike = set(), set()
        while count != len(workers):
            dist, worker, bike = heapq.heappop(heap)
            if worker not in used_worker and bike not in used_bike:
                res[worker] = bike
                used_worker.add(worker)
                used_bike.add(bike)
                count += 1
            else:
                heapq.heappush(heap, heapq.heappop(dists[worker]))
        return res

    def get_distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

sol = Solution()

workers = [[0,0], [2,1]]
bikes = [[1,2], [3,3]]
for a, b in zip(sol.assignBikes(workers, bikes), [1, 0]):
    assert a == b


workers = [[0,0], [1,1], [2,0]]
bikes = [[1,0], [2,2], [2,1]]
for a, b in zip(sol.assignBikes(workers, bikes), [0, 2, 1]):
    assert a == b
