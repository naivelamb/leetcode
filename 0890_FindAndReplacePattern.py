"""
https://leetcode.com/problems/find-and-replace-pattern/

Build a hashmap between pattern and word, if a new hash relashionship shows up, make sure both letters do not show before.

Time complexity: O(NP)
N = len(words), P = len(pattern)
"""
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            ref, seen = {}, set()
            flag = True

            for c, p in zip(word, pattern):
                if p in ref:
                    if ref[p] != c:
                        flag = False
                        break
                else:
                    if c in seen:
                        flag = False
                        break
                    else:
                        ref[p] = c
                        seen.add(c)

            if flag: ans.append(word)
        return ans