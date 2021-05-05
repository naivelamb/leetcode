"""
https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/s

DFS, be careful about "1000000"
"""
class Solution:
    def splitString(self, s: str) -> bool:
        dp = {}
        def helper(i, target):
            if i == len(s):
                return True            
            if target < 0:
                return False
            if (i, target) in dp:
                return dp[(i, target)]
            if target == 0:
                return int(s[i:]) == 0
            k = len(str(target)) - 1
            if k > 0:
                val = int(s[i:i+k])
            else:
                val = 0
            for j in range(i + k, len(s)):
                val = val * 10 + int(s[j])
                if val > target:
                    dp[(i, target)] = False
                    return False
                elif val == target:
                    return helper(j+1, target - 1)
            dp[(i, target)] = False
            return False
        
        for i in range(1, len(s)):
            if helper(i, int(s[:i]) - 1):
                return True
        return False
        
        