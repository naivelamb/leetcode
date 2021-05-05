"""
https://leetcode.com/problems/maximum-building-height/
"""
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.sort()
        
        #preprocessing - in case some restrictions are extremely low 
        for i in reversed(range(len(restrictions)-1)): 
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + restrictions[i+1][0] - restrictions[i][0])
        
        restrictions = [[1, 0]] + restrictions
        
        ans = 0 
        for i in range(1, len(restrictions)): 
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + restrictions[i][0] - restrictions[i-1][0])
            ans = max(ans, (restrictions[i-1][1] + restrictions[i][0] - restrictions[i-1][0] + restrictions[i][1])//2)
        ans = max(ans, restrictions[-1][1] + n - restrictions[-1][0])
        return ans 
        