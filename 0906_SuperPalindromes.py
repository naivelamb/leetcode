"""
https://leetcode.com/problems/super-palindromes/

Locate the search intervals, then search all possible numbers. 

Let's say P=R^2 is superpalindrome, then R is palindrome, hence 
let k = len(R) // 2
If len(R) % 2 == 0, then R = R[:k] + R[:k][::-1]
else, then R = R[:k+1] + R[:k][::-1]

Brute force search all possible candiates. 

"""
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L, R = int(left), int(right)
        MAGIC = 100000

        ans = 0
        for k in range(MAGIC):
            s = str(k)
            t = s + s[::-1]
            v = int(t) ** 2
            if v > R: break
            if v >= L and str(v) == str(v)[::-1]:
                ans += 1

        for k in range(MAGIC):
            s = str(k)
            t = s + s[:-1][::-1]
            v = int(t) ** 2
            if v > R: break
            if v >= L and str(v) == str(v)[::-1]:
                ans += 1   
        return ans     
