"""
https://leetcode.com/problems/boats-to-save-people/

At most 2 people can sit in one boat. We do it greedy, always try to pair the heaviest one with the lightest one.

Time complexity: O(NlogN)
"""
class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        people.sort()
        ans = 0
        i, j = 0, len(people) - 1
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans
