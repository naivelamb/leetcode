"""
https://leetcode.com/problems/perfect-squares/
BFS, the node is remain vals, minus the possible square nums to get next node vals.
Time complexity: O(n^(h/2)), h is the height of the N-array tree.
"""
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n

        square_nums = []
        i = 1
        while i **2 <= n:
            square_nums.append(i**2)
            i += 1

        count = 0
        left_vals = {n}
        while left_vals:
            count += 1
            tmp = set()
            for val in left_vals:
                for num in square_nums:
                    if num == val:
                        return count
                    if num > val:
                        break
                    tmp.add(val - num)
            left_vals = tmp
        return count
