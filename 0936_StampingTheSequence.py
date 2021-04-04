"""
https://leetcode.com/problems/stamping-the-sequence/

"""
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m = len(target), len(stamp)
        t, s, res = list(target), list(stamp), []
        def check(i):
            # keep trying changing letters to '?' starting from i
            # return True if nothing changed
            changed = False
            for j in range(m):
                if t[i+j] == '?': continue
                if t[i+j] != s[j]: return False
                changed = True
            if changed:
                t[i: i+m] = ['?'] * m
                res.append(i)
            return changed
        
        changed = True
        while changed:
            changed = False
            for i in range(n - m + 1):
                if check(i):
                    changed = True
        return res[::-1] if t == ['?'] * n else []