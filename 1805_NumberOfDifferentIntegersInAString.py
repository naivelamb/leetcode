"""
https://leetcode.com/problems/number-of-different-integers-in-a-string/

Python string operatin.
"""
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ans = ''
        for ch in word:
            if ch.isdigit():
                ans += ch
            else:
                ans += " "
        
        ans = ans.split(" ")
        res = set()
        for w in ans:
            if w: res.add(int(w))
        return len(res)