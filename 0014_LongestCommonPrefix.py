"""
https://leetcode.com/problems/longest-common-prefix/

Compare one by one. 
Time complexiy: O(N*W), N = len(strs), W = len(str)
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        def find_prefix(a, b):
            ans = ""
            for i in range(min(len(a), len(b))):
                if a[i] == b[i]:
                    ans += a[i]
                else:
                    break
            return ans
        
        ans = strs[0]
        for i in range(1, len(strs)):
            ans = find_prefix(ans, strs[i])
            if not ans:
                return ans
        return ans