# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/dota2-senate/

A senate can vote, ban and declare victory. 
We need to count the number of available votes and bans. 

Time complexity: O(n)

"""
import collections
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = collections.deque()
        people, bans = [0, 0], [0, 0]
        
        for person in senate:
            x = person == 'R'
            people[x] += 1
            queue.append(x)
        
        while all(people):
            x = queue.popleft()
            people[x] -= 1
            
            if bans[x]: # check whether the senate is banned
                bans[x] -= 1
            else: # not banned, he can ban others and save his vote
                bans[x^1] += 1
                queue.append(x)
                people[x] += 1
        
        return 'Radiant' if people[1] else 'Dire'