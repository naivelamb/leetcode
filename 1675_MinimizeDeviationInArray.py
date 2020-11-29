"""
https://leetcode.com/problems/minimize-deviation-in-array/

Odd can only multiply by 2, while even can be divided by 2. 
So we double all odd first, then we can only divide. 

Then we use a pq to monitor the array, we keep trying to make curr_max smaller (since all is even now, which can be smaller by dividing). 
When we encounter an odd number, we stop here, since any futher dividing cannot reduce the maximum.

Time complexity: O(nlogn)
"""
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        for n in nums:
            heapq.heappush(pq, -n * 2 if n % 2 else -n)
        low = -max(pq)
        res = float('inf')
        while len(pq) == len(nums):
            a = -heapq.heappop(pq)
            res = min(res, a - low)
            if a % 2 == 0:
                low = min(low, a//2)
                heapq.heappush(pq, -a//2)
        return res