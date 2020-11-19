"""
https://leetcode.com/problems/decode-string/

4 type of chars: '[', ']', num, letter.

Num could be consecutive, so when we see num, need to store it, next one, we will do num = num * 10 + curr_num

'[' means start of a pattern, we need to reset tempNum and tempPattern.

']' means end of a pattern, we need to assemble based on current pattern and current num, attach to last pattern.

char is just adding to curr pattern. 

This could be solved by a stack. In it, we will have [..., prev_string, num_for_next_pattern]. 

Time complexity: O(N)
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currNum = 0
        currString = ''

        for c in s:
            if c == '[':
                stack.append(currString)
                satck.append(currNum)
                currString = ''
                currNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                currString = prevString + currString * num
            elif c.isdigit():
                currNum = currNum * 10 + int(c)
            else:
                currString += c

        return currString