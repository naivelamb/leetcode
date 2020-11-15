"""
https://leetcode.com/problems/determine-if-two-strings-are-close/

The two words could be close if they:
1. have same length
2. contain same characters
3. have same amount of characters that are of same count

Time comlexity: O(N)
"""
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        cnt1, cnt2 = {}, {}
        for a, b in zip(word1, word2):
            cnt1[a] = cnt1.get(a, 0) + 1
            cnt2[b] = cnt2.get(b, 0) + 1

        ref1, ref2 = collections.defaultdict(list), collections.defaultdict(list)
        for c in cnt1:
            ref1[cnt1[c]].append(c)
            if c not in cnt2:
                return False
        for c in cnt2:
            ref2[cnt2[c]].append(c)
            if c not in cnt1:
                return False
        
        for k in ref1:
            if len(ref1[k]) != len(ref2[k]):
                return False
        return True