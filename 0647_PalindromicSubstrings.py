"""
https://leetcode.com/problems/palindromic-substrings/

DP[i][j] = True => s[i:j] is palindrome. 
DP[i][j] is palindrome, if DP[i+1][j-1] = True and s[i] == s[j-1]

Sum dp[i][j] == True

Time complexity: O(N^2), N = len(s)

Actually we can do it without DP array. Just choose center and then expand.
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        ans = 0
        
        for center in range(n):
            l, r = center, center
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    ans += 1
                else:
                    break

            l, r = center, center + 1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    ans += 1
                else:
                    break
        return ans