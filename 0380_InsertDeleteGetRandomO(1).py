# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/insert-delete-getrandom-o1/

Swap position when removing something in bewteen
"""

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.pos = {}

    def insert(self, val: 'int') -> 'bool':
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos:
            return False
        self.vals.append(val)
        self.pos[val] = len(self.vals) - 1
        return True
    
    def remove(self, val: 'int') -> 'bool':
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos:
            return False
        i, j = self.pos[val], self.pos[self.vals[-1]]
        if i != j: # swap
            self.vals[i] = self.vals[-1]
            self.pos[self.vals[i]] = i
        del self.pos[val]
        self.vals.pop()
        return True
        
    def getRandom(self) -> 'int':
        """
        Get a random element from the set.
        """
        return random.choice(self.vals)