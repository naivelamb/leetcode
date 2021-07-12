"""
https://leetcode.com/problems/reduce-array-size-to-the-half/

Count elements, sort by freq, remove from most ones. 

Time complexity: O(n + klogk)
n = len(arr)
k = num of distinct elements
"""
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = collections.Counter(arr)
        n = len(arr)
        cnts = sorted(cnt.values())
        remain_n, ans = n, 0
        while remain_n > n // 2:
            remain_n -= cnts.pop()
            ans += 1
        return ans