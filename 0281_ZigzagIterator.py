# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/zigzag-iterator/

Use a flag to identify which array we are pointing to. 
"""
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1[::-1]
        self.v2 = v2[::-1]
        self.first = True
    
    def next(self):
        """
        :rtype: int
        """
        if self.first:
            self.first = False
            return self.v1.pop()
        else:
            self.first = True
            return self.v2.pop()
    
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.first:
            if self.v1:
                return True
            else:
                self.first = False
                if self.v2:
                    return True
                else:
                    return False
        else:
            if self.v2:
                return True
            else:
                self.first = True
                if self.v1:
                    return True
                else:
                    return False
