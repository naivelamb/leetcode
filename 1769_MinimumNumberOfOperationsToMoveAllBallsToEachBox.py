"""
https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

For a box i, the total cost is move all left boxes to it and all right boxes to it. 

We can first calculate the cost to move all boxes to 0.

Then for any i, and if we know the costs to for (i-1) -> ans[i-1], number of 1 in the left, and number of 1 in the right, then
ans[i] = ans[i-1] + left - right
Since compared to ans[i-1], we need to move all left one more step, all right one less step. 

Time complexity: O(N)
"""
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n_ones, i_sum = 0, 0
        for i, ch in enumerate(boxes):
            if ch == '1':
                n_ones += 1
                i_sum += i
        
        ans = []
        n_left, n_right = 0, n_ones
        for ch in boxes:
            if not ans:
                val = i_sum
            else:
                val = ans[-1] + n_left - n_right
            ans.append(val)
            if ch == '1':
                n_left += 1
                n_right -= 1
        return ans