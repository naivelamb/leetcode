"""
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

There are 2**k binary codes of length k. So we just need to check number of distinct substring of length k from s. 

Time complexity: O(N)

"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substring = set()
        for i in range(len(s) - k + 1):
            substring.add(s[i:i+k])

        return len(substring) == 2**k