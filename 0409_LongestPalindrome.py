"""
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3423/

Count characters.
Time Complexity: O(N), N=len(s)
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        ref = {}
        for c in count:
            ref[count[c]] = ref.get(count[c], 0) + 1
        ans = 0
        odd = False
        for n in ref:
            if n % 2 == 1:
                ans += ref[n] * (n - 1)
                if not odd:
                    ans += 1
                    odd = True
            else:
                ans += ref[n] * n
        return ans
