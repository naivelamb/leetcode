"""
https://leetcode.com/problems/create-sorted-array-through-instructions/

Segment tree, use Binary Indexed Tree here.

Binary Indexed Tree/Fenwick Tree
Represent an array of numbers in an array, allowing prefix sum to be calculated efficiently. 

Given an array A, and two types of operations are allowed:
1. Change the value stored at an index i. ==> point update
2. Find the sum of a prefix of length k. ==> range sum
Mutable range/prefix sum problem. 

If one use dp to do it, build the data structure is O(N), query is O(1). But when update takes O(N), making it inefficient. 

By using Binary Indexed Tree or Segment Tree, both opeartions will be O(logN), which is perfect when the data is huge. 

IN BIT, at any index we store the sum of some numbers of the given array. 
BIT[x] =  a[x] if x is odd
          a[1] + ... + a[x] if x is power of 2
To generalize, every index i in BIT stores the cumulative sum from the index i to (i - (1 << r) + 1), where r is the last set bit in the index i. [last_set_bit of x = x&-x]

Hence, we can write the pseudo code
update(i, val) => add "val" to index "i":
  while i <= n:
      BIT[i] += val
      i += i & (-i)

query(i) => sum of first i elements:
  total = 0
  while i > 0:
      total += BIT[i]
      i -= i & (-i)
  return total


Time complexity: O(NlogM), M is the range of instructions[i]
"""
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        m = max(instructions)
        c = [0] * (m + 1)

        def update(x):
            while (x <= m):
                c[x] += 1
                x += x & -x
        
        def get(x):
            res = 0
            while (x > 0):
                res += c[x]
                x -= x & -x
            return res
        
        res = 0
        for i, a in enumerate(instructions):
            res += min(get(a - 1), i - get(a))
            update(a)
        return res % (10 ** 9 + 7)