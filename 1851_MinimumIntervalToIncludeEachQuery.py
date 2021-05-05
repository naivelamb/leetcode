"""
https://leetcode.com/problems/minimum-interval-to-include-each-query/

Sort queries and intervals, interate queries from small to big.
Find all open intervals [l, r] and add them to a pq.
Also remove all closed intervals from the pq. 

Time complexity: O((n+q)logn)
"""
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals)[::-1]
        h = []
        ref = {}
        for q in sorted(queries):
            while intervals and intervals[-1][0] <= q:
                i, j = intervals.pop()
                if j >= q:
                    heapq.heappush(h, [j-i+1, j])
            while h and h[0][1] < q:
                heapq.heappop(h)
            ref[q] = h[0][0] if h else -1
        return [ref[q] for q in queries]