# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/number-of-squareful-arrays/

We first get the count and all possible squareful pairs. 
Then generate the squareful arrays using DFS. 
The generation process is basically a permutation with duplication.
"""
import collections
class Solution:
    def numSquarefulPerms(self, A: 'List[int]') -> 'int':
        cnt = collections.Counter(A)
        sq_pairs = collections.defaultdict(list)
        for x in cnt:
            for y in cnt:
                if int((x + y)**0.5) == (x + y)**0.5:
                    sq_pairs[x] += [y] * (cnt[y] - (x == y))
                
        self.res = 0
        def dfs(last):
            if sum(cnt.values()) == 0:
                self.res += 1
            next_nums = sq_pairs.get(last)
            for i, next_num in enumerate(next_nums):
                if i > 0 and next_nums[i - 1] == next_num:
                    continue
                if cnt[next_num] > 0:
                    cnt[next_num] -= 1
                    dfs(next_num)
                    cnt[next_num] += 1
            
        for x in sq_pairs:
            cnt[x] -= 1
            dfs(x)
            cnt[x] += 1

        return self.res

s = Solution()
A = [2, 2, 2]
print(s.numSquarefulPerms(A))
A = [8, 17, 1]
print(s.numSquarefulPerms(A))
A = [1, 17, 8, 8]
print(s.numSquarefulPerms(A))
A = [1,1,1,1,1,1,1,1,1,1,1]
print(s.numSquarefulPerms(A))
A = [2,2,2,2,2,2,2,2,2]
print(s.numSquarefulPerms(A))