"""
https://leetcode.com/problems/poor-pigs/

We can test N rounds, N = minutesToTest // minutesToDie

A pig can have (N+1) states through out the test: Die or not at each round and alive at the end. 

Hence given x pigs, the total states we can represent is: (N+1)^x. 

So we need to find minimum x, such that (N+1)^x >= buckets
"""
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        x = 0
        while (minutesToTest//minutesToDie + 1)**x < buckets:
            x += 1
        return x