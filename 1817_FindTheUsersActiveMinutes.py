"""
https://leetcode.com/problems/finding-the-users-active-minutes/

Built user active minutes dictionary. Then just look through the dict. 

Time complexity: O(N)
"""
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ref = collections.defaultdict(set)
        for u, m in logs:
            ref[u].add(m)
        
        ans = [0] * k
        
        for u in ref:
            m = len(ref[u])
            ans[m - 1] += 1
        
        return ans