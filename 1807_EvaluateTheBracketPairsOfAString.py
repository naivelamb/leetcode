"""
https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

Put knowledge into a hashtable, just check whether the words in bracket are in the hashtable or not. 

Time complexity: O(m+n)
"""
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        ref = {k:v for k, v in knowledge}

        ans, prev = '', -1
        for i, ch in enumerate(s):
            if ch == '(':
                prev = i
            elif ch == ')':
                tmp = s[prev + 1: i]
                ans += ref.get(tmp, '?')
                prev = -1
            else:
                if prev == -1:
                    ans += ch
        return ans