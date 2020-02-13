"""
https://leetcode.com/problems/ambiguous-coordinates/

First split S into two parts.
Then find all the possible places to place decimal points.
"""
class Solution:
    def ambiguousCoordinates(self, S: str):
        def build(S):
            # given a string S, return all possible numbers.
            ans = []
            if S.startswith('0') or S.endswith('0'):
                if S == '0':
                    ans = [S]
                elif S.startswith('0') and S.endswith('0'):
                    ans = []
                elif S.endswith('0'):
                    ans = [S]
                else: # S.startswith('0'):
                    ans = [S[0] + '.' + S[1:]]
            else:
                ans = [S]
                for i in range(1, len(S)):
                    ans.append(S[:i] + '.' + S[i:])
            return ans
            
        S = S[1:-1] # stripe '()'
        ans = []
        for i in range(1, len(S)):
            left, right = build(S[:i]), build(S[i:])
            tmp = []
            for cand1 in left:
                for cand2 in right:
                    tmp.append(f"({cand1}, {cand2})")
            ans += tmp
        return ans

sol = Solution()
assert sol.ambiguousCoordinates('(123)') == ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
assert sol.ambiguousCoordinates('(00011)') == ["(0.001, 1)", "(0, 0.011)"]
assert sol.ambiguousCoordinates('(0123)') == ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
assert sol.ambiguousCoordinates('(100)') == ["(10, 0)"]
