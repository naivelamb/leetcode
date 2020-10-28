"""
https://leetcode.com/problems/student-attendance-record-i/

Go through the record.
Time complexity: O(N)
"""
class Solution:
    def checkRecord(self, s: str) -> bool:
        cntA, cntL = 0, 0
        for i, c in enumerate(s):
            if c == 'A':
                cntA += 1
            if c == 'L':
                if i > 0 and s[i-1] == 'L':
                    cntL += 1
                else:
                    cntL = 1
            if cntA > 1 or cntL > 2:
                return False
        return True