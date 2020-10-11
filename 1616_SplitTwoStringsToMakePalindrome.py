"""
https://leetcode.com/problems/split-two-strings-to-make-palindrome/

We are supposed to split at the same index, so we know the mid position and potential pattern.

We can build a helper function to check if a[:mid] can be used to build the palindrome. The function would check for any i < len(a) - mid, if a[mid:mid+i] == a[mid:mid-i][::-1], if so we keep traverse until it does not satisfy. Then we would check if we can fill the rest part from b.

We can call the above function 4 times to check palindrome formation.

Time complexity: O(4N)
"""
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if a == a[::-1] or b == b[::-1]:
            return True

        def helper(a, b):
            mid = len(a) // 2
            if len(a) % 2 == 1:
                # skip mid
                pattern = a[:mid]
                start = mid + 1
            else:
                pattern = a[:mid]
                start = mid
            p1, p2 = mid - 1, start
            while a[p1] == a[p2] and p1 >= 0 and p2 < len(a):
                p1 -= 1
                p2 += 1
            return a[:p1+1] == b[p2:][::-1]

        if helper(a, b) or helper(b, a) or helper(a[::-1], b[::-1]) or helper(b[::-1], a[::-1]):
            return True
        return False
