"""
https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

Counter number of incorrect postitions. 
Let 
dp1 := # of incorrect digits if target starts with '0'; 
dp2 := # of incorrect digits if target starts with '1'.
dp1 + dp2 = len(s)

After op1, new dp1, dp2 can be derived from previous dp1, dp2. 

If n % 2 == 0 => dp1, dp2 = prev_dp2, prev_dp1
Else,
if current ch == '0', 
dp1 = n - 1 - dp1, dp2 = n + 1 - dp2
else,
dp1 = n + 1 - dp1, dp2 = n - 1 - dp2

ans = min(ans, min(dp1, dp2))

Time complexity: O(n)
"""
class Solution:
    def minFlips(self, s: str) -> int:
        cnt1 = 0
        for i, x in enumerate(s):
            if i % 2 and x != '1':
                cnt1 += 1
            elif i % 2 == 0 and x != '0':
                cnt1 += 1
        cnt2 = len(s) - cnt1
        # cnt1 => # of miss for 0101 
        # cnt2 => # of miss for 1010
        ans = min(cnt1, cnt2)
        
        n = len(s)
        for ch in s:
            if ch == '0':
                if n % 2 == 0:
                    cnt1, cnt2 = cnt2, cnt1
                else:
                    cnt1, cnt2 = n - 1 - cnt1, n + 1 - cnt2
            else:
                if n % 2 == 0:
                    cnt1, cnt2 = cnt2, cnt1
                else:
                    cnt1, cnt2 = n + 1 - cnt1, n - 1 - cnt2
            ans = min(ans, min(cnt1, cnt2))
        return ans