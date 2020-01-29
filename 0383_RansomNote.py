"""
https://leetcode.com/problems/ransom-note/

Check the character count in magazine.
Time complexity: O(m + n). m = len(ransomNote), n = len(magazine)
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1

        for ch in ransomNote:
            if ch not in count:
                return False
            else:
                count[ch] -= 1
                if count[ch] < 0:
                    return False
        return True

sol = Solution()
assert sol.canConstruct("a", "b") == False
assert sol.canConstruct("aa", "ab") == False
assert sol.canConstruct("aa", "aab") == True
