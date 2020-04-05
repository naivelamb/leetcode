"""
https://leetcode.com/problems/zigzag-conversion/
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = []
        pos = 0
        row = 0
        if numRows == 1:
            return s
        while pos < len(s):
            k = row % (numRows - 1)
            if k == 0:
                tmp = list(s[pos: pos + numRows])
                if pos + numRows >= len(s):
                    tmp += [''] * (pos+numRows - len(s))
                    pos += len(tmp)
                else:
                    pos += len(tmp)
            else:
                tmp = [''] * numRows
                tmp[numRows - k - 1] = s[pos]
                pos += 1
            row += 1
            ans.append(tmp)
        final_ans = ''
        for i in range(numRows):
            final_ans += ''.join([ans[k][i] for k in range(len(ans))])
        return final_ans 

sol = Solution()
assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
