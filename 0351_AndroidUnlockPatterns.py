# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/android-unlock-patterns/

1 | 2 | 3
4 | 5 | 6
7 | 8 | 9

Let f(n) gives all the possible patterns for n-keys. 
Then we can generate f(n+1) based on f(n).

For example, '123' is a pattern for f(3), the next pattern can be:
'123' + '2' -> invalid
'123' + '5'
'123' + '6' 
'123' + '4' -> knight jump
'123' + '8' -> knight jump

To make the process easier, we need to build a ref graph indicating the relation
between current node and next node.

-------------------------------------------
Optimized method:
We don't care about the exact string since we only care about the number of pattern.
What we need is 'used_num', 'last_num'. 

The numbers can be distinguished into 3 groups:
    corner: 1, 3, 7, 9
    mid: 2, 4, 6, 8
    center: 5
Obviously, 5 can visit all other numbers.
For a corner number, take 1 as example, it can visit neighbors (2, 4, 5) and
knight jump (6, 8) freely. It can visit 9 if 5 is visited, (3, 7) if (2, 4) is 
visited.
For a mid number, take 2 as example, it can visit neighbors (1, 3, 4, 5, 6) and
(7, 9) freely. It can visit 8 if 5 is visited. 
Therefore, given a last number, we can visit all other remain numbers. 

"""
import collections
class Solution:
    def numberOfPatterns(self, m: 'int', n: 'int') -> 'int':
        visited = {}
        self.res = 0
        self.corner = {1, 3, 7, 9}
        self.mid = {2, 4, 6, 8}
        for i in range(1, 10):
            visited[i] = 1
            self.dfs(visited, 1, m, n, i)
            del visited[i]
        return self.res
    
    def dfs(self, visited, keys, m, n, prev):
        if m <= keys <= n:
            self.res += 1
        if keys == n:
            return
        for next_num in range(1, 10):
            if next_num not in visited:
                if prev in self.corner and next_num in self.corner and (prev + next_num) // 2 not in visited:
                    continue
                elif prev in self.mid and next_num == (10 - prev) and 5 not in visited:
                    continue
                visited[next_num] = 1
                self.dfs(visited, keys + 1, m, n, next_num)
                del visited[next_num]
    
    def numberOfPatterns_Naive(self, m: 'int', n: 'int') -> 'int':
        ref = {'1': '24568',
               '2': '1345679',
               '3': '24568',
               '4': '1235789',
               '5': '12346789',
               '6': '1235789',
               '7': '24568',
               '8': '1345679',
               '9': '24568'}
        
        memo = collections.defaultdict(set)
        memo[1] = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        def dp(n):
            # return all possible pattern for n-keys
            if n in memo:
                return memo[n]
            else:
                res = set()
                for p in dp(n - 1):
                    for c in ref[p[-1]]:
                        if c not in p:
                            res.add(p + c)
                        else:
                            c_jump = 2 * int(c) - int(p[-1])
                            if 1 <= c_jump <= 9 and str(c_jump) not in p:
                                res.add(p + str(c_jump))
                memo[n] = res
                return memo[n]
        for i in range(m, n + 1):
            dp(i)
        return sum(len(memo[i]) for i in range(m, n + 1))

s = Solution()
print(s.numberOfPatterns(3, 3))