"""
https://leetcode.com/problems/add-binary/
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        ans = []
        add_one = 0
        for i in range(max(len(a), len(b))):
            if i < len(a):
                v1 = int(a[i])
            else:
                v1 = 0
            if i < len(b):
                v2 = int(b[i])
            else:
                v2 = 0
            val = v1 + v2 + add_one
            ans.append(str(val % 2))
            if val // 2 == 1:
                add_one = 1
            else:
                add_one = 0

        if add_one:
            ans.append('1')
        return ''.join(ans[::-1])
