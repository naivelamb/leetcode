"""
https://leetcode.com/problems/minimize-max-distance-to-gas-station/
1) Brute force with Heap
Find the biggest gap, insert a station.
Use a heap to maintain the distance - station pair info.
Time complexity:
O(Klog(N))

2) Binary search
Let's say we have the answer D, to make it possible, for each interval with length X,
we need to insert math.ceil(X/D) stations to make it possible.
We need to make sure the total amount of stations we added does not exceed K.
So we need to search all the possible answers from 1e-6 to (stations[-1] - stations[0]).

Time complexity: O(NlogW), W = (stations[-1] - stations[0])/10^-6
"""
import heapq
class Solution:
    def minmaxGasDist(self, stations, K: int) -> float:
        left, right = 1e-6, stations[-1] - stations[0]
        while left + 1e-6 < right:
            mid = (left + right) / 2
            count = 0
            for a, b in zip(stations, stations[1:]):
                count += math.ceil((b - a)/mid) - 1
            if count > K:
                left = mid
            else:
                right = mid
        return right

    def minmaxGasDist_heap(self, stations, K: int) -> float:
        dist = []
        for i in range(1, len(stations)):
            dist.append((- stations[i] + stations[i-1], stations[i] - stations[i-1], 1))
        heapq.heapify(dist)

        while K:
            d, l, n = heapq.heappop(dist)
            n += 1
            d = -l/n
            #print(d, l, n)
            heapq.heappush(dist, (d, l, n))
            K -= 1

        ans, _, _ = heapq.heappop(dist)
        return -ans

sol = Solution()
stations = [1,2,3,4,5,6,7,8,9,10]
assert abs(sol.minmaxGasDist_heap(stations, 9) - 0.5) < 1e-6
stations = [10,19,25,27,56,63,70,87,96,97]
#assert abs(sol.minmaxGasDist_heap(stations, 3) - 9.6667) < 1e-6
