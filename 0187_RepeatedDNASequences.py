"""
https://leetcode.com/problems/repeated-dna-sequences/

Sliding window, count all subsequence, record the ones show more than once.

Time complexity: O(10N)
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        if n <= 10:
            return ans
        curr_window = collections.deque(list(s[:10]))
        count = {s[:10]: 1}
        for i in range(10, n):
            curr_window.popleft()
            curr_window.append(s[i])
            sub = ''.join(curr_window)
            count[sub] = count.get(sub, 0) + 1
            if count[sub] == 2:
                ans.append(sub)
        return ans        
