"""
https://leetcode.com/problems/isomorphic-strings/

Two hashmap, one record s->t mapping, the other t->s mapping. 
Chech character by character, add to mapping if not exist. 

Time complexity: O(N)
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st, map_ts = {}, {}
        for a, b in zip(s, t):
            if a in map_st and b in map_ts:
                if map_st[a] != b or map_ts[b] != a:
                    return False
            else:
                if a in map_st or b in map_ts:
                    return False
                map_st[a] = b
                map_ts[b] = a
        return True