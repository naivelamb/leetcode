"""
https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

(a1^a2) & (b1^b2) = (a1&b1) ^ (a1&b2) ^ (a2&b1) ^ (a2&b2)

So we do AND for arr1 and arr2 respectively, then do XOR.

Time complexity: O(m + n)
"""
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        out1 = arr1[0]
        for x in arr1[1:]:
            out1 ^= x
        
        out2 = arr2[0]
        for x in arr2[1:]:
            out2 ^= x
        return out1 & out2