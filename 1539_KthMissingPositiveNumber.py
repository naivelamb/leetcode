"""
https://leetcode.com/problems/kth-missing-positive-number/

Two pointers, record how many missing have been recorded.

Time complexity: O(min(K, len(arr))

"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        v, i, cnt = 1, 0, 0
        while True:
            if v == arr[i]:
                v += 1
                i += 1
            else:
                cnt += 1
                v += 1
            if cnt == k:
                return v