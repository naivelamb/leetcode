"""
https://leetcode.com/problems/count-sorted-vowel-strings/

#1 Math solution
For a given combination of vowel, the order is determined. This is a combination with replace problem. The results are 
C(n+r-1, n)

# DP solution
DP[n][k] number of strings constructed by at most k different characters. 
DP[n][k] = sum(DP[n-1, k]) for k in range(1, k+1))

Time complexity: O(nk)
"""
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return int(math.factorial(5 + n - 1)/math.factorial(n)/math.factorial(4))
    
    def countVowelStrings_dp(self, n):
        seen = {}
        def dp(n, k):
            if k == 1 or n == 1: return k
            if (n, k) in seen:
                return seen[n, k]
            seen[n, k] = sum(dp(n - 1, k) for k in range(1, k+1))
            return seen[n, k]
        return dp(n, 5)