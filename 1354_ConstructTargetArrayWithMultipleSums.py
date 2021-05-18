"""
https://leetcode.com/problems/construct-target-array-with-multiple-sums/

Everyround get the current maximum value, delete it by the sum of other element. 

Tim complexity: O(logMaxAlogN)
"""
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        A = [-a for a in target]
        heapq.heapify(A)
        while True:
            a = - heapq.heappop(A)
            total -= a
            if a == 1 or total == 1:
                return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(A, -a)