"""
https://leetcode.com/problems/backspace-string-compare/
1) 2-pointer
Move 2-pointer reversely. When we see '#', we keep going backwards untill we see a non-'#' char and record the steps.
Time complexity: O(N); Space: O(1) 
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        p1, p2 = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while p1 >= 0 and (backS or S[p1] == '#'):
                backS += 1 if S[p1] == '#' else -1
                p1 -= 1
            while p2 >= 0 and (backT or T[p2] == '#'):
                backT += 1 if T[p2] == '#' else -1
                p2 -= 1
            if not (p1 >= 0 and p2 >= 0 and S[p1] == T[p2]):
                return p1 == p2 == -1
            p1, p2 = p1 -1, p2 - 1

sol = Solution()
assert sol.backspaceCompare('ab#c', 'ad#c') == True
assert sol.backspaceCompare('ab##', 'c#d#') == True
assert sol.backspaceCompare('a##c', '#a#c') == True
assert sol.backspaceCompare('a#c', 'b') == False
