"""
https://leetcode.com/problems/vowel-spellchecker/

Build 3 dictionary. 

Time compleixty: O(M + N)
"""
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def mask(w):
            return ''.join('*' if c in 'aeiou' else c for c in w.lower())
        
        d0 = set(wordlist)
        d1 = {w.lower(): w for w in wordlist[::-1]}
        d2 = {mask(w): w for w in wordlist[::-1]}

        def slove(query):
            if query in d0: return query
            if query.lower() in d1: return d1[query.lower()]
            if mask(query) in d2: return d2[mask(query)]
            return ""
        return [slove(q) for q in queries]