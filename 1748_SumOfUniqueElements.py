"""
https://leetcode.com/problems/sum-of-unique-elements/

Count then sum all the elements with freq=1

Time complexity: O(n)
"""
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
        
        ans = 0
        for x in cnt:
            if cnt[x] == 1:
                ans += x
        return ans