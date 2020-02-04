"""
https://leetcode.com/problems/split-array-into-fibonacci-sequence/

Backtracking.
Try to add digit to current number, check whether fibonacci is built up, when
current number > ans[-1] + ans[-2], need to go back to modify
"""
class Solution:
    def splitIntoFibonacci(self, S: str):
        def isFiboEligible(s, ans, start_idx):
            if (start_idx == len(s) and len(ans) >= 3):
                return True

            for end_idx in range(start_idx + 1, len(s) + 1):
                current_number = int(s[start_idx:end_idx])
                current_number_digit = end_idx - start_idx
                # make sure the number does not start with '0'
                if (current_number_digit) > 1 and s[start_idx:end_idx][0] == '0':
                    return False
                if current_number > 2**31 - 1:
                    return False
                elif ((len(ans) >= 2) and (current_number > ans[-2] + ans[-1])):
                    return False
                elif ((len(ans) <= 1) or (current_number == ans[-2] + ans[-1])):
                    ans.append(current_number)
                    if isFiboEligible(s, ans, start_idx+current_number_digit):
                        return True
                    else:
                        ans.pop()
            return False

        answer = []
        isFiboEligible(S, answer, 0)
        return answer

sol = Solution()

S = '123456579'
assert sol.splitIntoFibonacci(S) == [123, 456, 579]
S = '11235813'
assert sol.splitIntoFibonacci(S) == [1, 1, 2, 3, 5, 8, 13]
S = '112358130'
assert sol.splitIntoFibonacci(S) == []
S = '0123'
assert sol.splitIntoFibonacci(S) == []
S = '1101111'
assert sol.splitIntoFibonacci(S) == [110, 1, 111]
