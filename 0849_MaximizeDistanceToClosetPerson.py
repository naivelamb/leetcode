"""
https://leetcode.com/problems/maximize-distance-to-closest-person/

Record the previous occupied postion, special treatment to head and tail. 

Time complexity: O(N)
"""
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans, prev = -float('inf'), None
        for i, state in enumerate(seats):
            if state == 1:
                if prev is None:
                    ans = i
                else:
                    ans = max(ans, (i - prev)//2)
                prev = i

        if seats[-1] == 0:
            ans = max(ans, len(seats) - prev - 1)
        return ans