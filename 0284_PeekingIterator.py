# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/peeking-iterator/

Store the next element as temp. If there is no next element, make it None. 
"""
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.temp = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.temp

    def next(self):
        """
        :rtype: int
        """
        res = self.temp
        self.temp = self.iter.next() if self.iter.hasNext() else None
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.temp is not None
