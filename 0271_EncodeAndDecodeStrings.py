# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/encode-and-decode-strings/

Encode as : word_length + '_' + word.
If word = 'xyz', encode it as '3_xyz'. 
"""

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for w in strs:
            res += str(len(w)) + '_' + w
        return res
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        pos, w_len = 0, 0
        while pos < len(s):
            if s[pos].isdigit():
                w_len = w_len * 10 + int(s[pos])
                pos += 1
                if s[pos] == '_':
                    res.append(s[pos + 1: pos + 1 + w_len])
                    pos += 1 + w_len
                    w_len = 0
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
        
s = Codec()
a = ["63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "]
a_encode = s.encode(a)
print(a_encode)
a_decode = s.decode(a_encode)
print(a_decode)