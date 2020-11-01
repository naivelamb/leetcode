"""
https://leetcode.com/problems/check-array-formation-through-concatenation/

Record the 'number-position' relation of arr, for each piece, check if it covers the subarray in original array. 
Time complexity: O(N)
"""

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        ref = {num:i for i, num in enumerate(arr)}
        for piece in pieces:
            if piece[0] not in ref:
                return False
            i = ref[piece[0]]
            for j in range(len(piece)):
                if i >= len(arr) or arr[i] != piece[j]:
                    return False
                i += 1
        return True