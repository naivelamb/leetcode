"""
https://leetcode.com/problems/random-pick-with-weight/

Transfer weight to prefix sum. When pick, generate a random number, then find the position using binary search.

init: O(N)
pick: O(logN)
"""
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = (low + high) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
