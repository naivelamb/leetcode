"""
https://leetcode.com/problems/top-k-frequent-elements/

Get count of all elements => O(N)
Store results in a heap => O(N)
Pop K element => O(KlogN)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref = {}
        for n in nums:
            ref[n] = ref.get(n, 0) + 1

        heap = []
        for key in ref:
            heap.append((-ref[key], key))
        heapq.heapify(heap)

        ans = []
        for _ in range(k):
            _, val = heapq.heappop(heap)
            ans.append(val)
        return ans
