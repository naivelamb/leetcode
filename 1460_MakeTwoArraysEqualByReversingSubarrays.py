"""
https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

Check number of elements. 

Time complexity: O(N)
"""
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False
        
        cnt = collections.Counter(target)
        for n in arr:
            cnt[n] -= 1
            if cnt[n] == -1:
                return False
        
        return True