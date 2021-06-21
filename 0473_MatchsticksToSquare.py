"""
https://leetcode.com/problems/matchsticks-to-square/

combination problem

Time complexity: O(4^N)
"""
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4 or sum(matchsticks) % 4 != 0:
            return False

        size = sum(matchsticks) // 4 # targe size
        matchsticks.sort(reverse=True)
        
        target = [size] * 4

        def dfs(matchsticks, pos, target):
            if pos == len(matchsticks): return True

            for i in range(4):
                if target[i] >= matchsticks[pos]:
                    target[i] -= matchsticks[pos]
                    if dfs(matchsticks, pos+1, target): return True
                    target[i] += matchsticks[pos]
            return False
        
        return dfs(matchsticks, 0, target)