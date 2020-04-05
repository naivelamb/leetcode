"""
https://leetcode.com/problems/longest-palindromic-substring/
dp[i][j] = 1 means s[i:j] is a palindrome.
dp[i][j] = 1 if s[i] == s[j] and dp[i+1][j-1] == 1.

Time complexity: O(n^2)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        ans = ""
        max_length = 0
        for i in range(n):
            dp[i][i] = 1
            max_length = 1
            ans = s[i]
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                ans = s[i:i+2]
                max_length=2
        for j in range(n):
            for i in range(j-1):
                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                    if max_length < j - i + 1:
                        max_length = j - i + 1
                        ans = s[i:j+1]
        return ans

sol = Solution()
assert sol.longestPalindrome('babad') == 'bab'
assert sol.longestPalindrome('bb') == 'bb'
