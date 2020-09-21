"""
https://leetcode.com/problems/rearrange-spaces-between-words/

Count the spaces, then re-arrange.

Time Complexity: O(N)
"""
class Solution:
    def reorderSpaces(self, text: str) -> str:
        new_text = text.split()
        n_spaces = len(text) - len(''.join(new_text))
        if len(new_text) == 1:
            return new_text[0] + " " * n_spaces
        cnt = n_spaces // (len(new_text) - 1)
        ans = (" " * cnt).join(new_text)
        ans += (n_spaces % (len(new_text) - 1)) * " "

        return ans
