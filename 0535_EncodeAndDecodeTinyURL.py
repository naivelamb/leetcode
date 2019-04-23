# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/encode-and-decode-tinyurl/

Store the short-long url pair in a hashmap.
Short url is encoded randomly by choosing random letters and digits. 
We keep random shuffle untill the key is not contained in the hashmap.

"""
import random
import string

class Codec:
    def __init__(self):
        self.url_pair = {}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        suffix_set = string.ascii_letters + string.digits
        key = ''.join(random.choice(suffix_set) for _ in range(6))
        while key in self.url_pair:
            key = ''.join(random.choice(suffix_set) for _ in range(6))
            
        tiny_url = "http://tinyurl.com/" + key
        
        self.url_pair[tiny_url] = longUrl
        
        return tiny_url
    
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.url_pair[shortUrl]    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
