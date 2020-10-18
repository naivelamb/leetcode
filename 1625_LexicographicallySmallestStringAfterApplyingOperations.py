"""
https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

Use stack to record the current position, set to record the seen one. Try all possible operations.

"""
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def op1(nums, a):
            nums = list(nums)
            for i, n in enumerate(nums):
                if i % 2 == 1:
                    nums[i] = (int(n) + a) % 10
            return ''.join(map(str, nums))
        
        def op2(nums, b):
            return nums[b:] + nums[:b]
        
        ans, seen = s, set()
        stack = [s]
        while stack:
            s = stack.pop()
            if s in seen:
                continue
            else:
                ans = min(s, ans)
                seen.add(s)
                s1, s2 = op1(s, a), op2(s, b)
                if s1 not in seen:
                    stack.append(s1)
                if s2 not in seen:
                    stack.append(s2)
        return ans