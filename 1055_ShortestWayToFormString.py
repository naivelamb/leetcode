# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/shortest-way-to-form-string/

If the target contains a char that does not exist in source, return -1.

If there is possible solution, we need to use one subsequence to cover the
target as long as possible, then start to use next subsequence (greedy). We use
two pointer to do this.

1) If target[p_t] == source[p_s] ==> p_t += 1, p_s += 1
2) Else, p_s += 1
3) If p_s == len(source) ==> ans += 1, p_s = 0
4) At last, check if ans += (p_s != 0)

Method 2:
If we know next avaiable position, we can jump faster!
"""

class Solution:
    def shortestWay(self, source, target):
        # check whether there is an answer
        ch_source = set(source)
        for t in target:
            if t not in ch_source:
                return -1
        # find the answer
        ans = 0
        p_source, p_target = 0, 0
        while p_source < len(source) and p_target < len(target):
            if target[p_target] == source[p_source]:
                p_target += 1
                p_source += 1
            else
                p_source += 1
            if p_source == len(source):
                ans += 1
                p_source = 0

        if p_source != 0:
            ans += 1
        return ans

    def shortestWay2(self, source, target):
        # store information into a hashmap
        import collections
        from bisect import bisect
        hashmap = collections.defaultdict(list)
        for i, s in enumerate(source):
            hashmap[s].append(i)
        ans, pointer = 1, -1
        for c in target:
            if c not in hashmap:
                return -1

            j = bisect(hashmap[c], pointer)
            if j >= len(hashmap[c]):
                pointer = hashmap[c][0]
                ans += 1
            else:
                pointer = hashmap[c][j]
        return ans
        
sol = Solution()
source = "abc"
target = "abcbc"
assert sol.shortestWay(source, target) == 2

source = "abc"
target = "acdbc"
assert sol.shortestWay(source, target) == -1

source = "xyz"
target = "xzyxz"
assert sol.shortestWay(source, target) == 3
