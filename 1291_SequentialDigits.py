"""
https://leetcode.com/problems/sequential-digits/

Fix the starting digit, then keep adding, record all numbers that fits the requirements.

Time Compelxity: O(10N), where N = len(str(high))
"""
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ref_ans = collections.defaultdict(list)
        for start_digit in range(1, 10):
            curr_n = start_digit
            val = start_digit
            n = 1
            while val <= high and curr_n < 10:
                if val >= low:
                    ref_ans[n].append(val)
                curr_n += 1
                val = val * 10 + curr_n
                n += 1
        ans = []
        for v in ref_ans:
            ans += ref_ans[v]
        return ans
