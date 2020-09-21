"""
https://leetcode.com/problems/car-pooling/

Sort the candidate, go from the first start locations. Use a heap to record the on-board passagers.

At each location, let passager get off, then pick up passagers. Check whether we exceed the capaity.

Time Compleixty: O(NlogN).
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: (x[1], x[2]))
        curr_passagers = 0
        heap = []
        for num, s, e in trips:
            while heap and s >= heap[0][0]:
                _, n = heapq.heappop(heap)
                curr_passagers -= n

            curr_passagers += num
            heapq.heappush(heap, (e, num))
            if curr_passagers > capacity:
                return False

        return True
