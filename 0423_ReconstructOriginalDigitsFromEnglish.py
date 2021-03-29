"""
https://leetcode.com/problems/reconstruct-original-digits-from-english/

Remove by order
z -> zero
w -> two
u -> four
g -> eight
x -> six

o -> one
t -> three
f -> five
s -> seven
n -> nine

Time complexity: O(n)
"""
class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = Counter(s)
        digits = ["zero", "two", "four", "six",  "eight", "one", "three", "five", "seven", "nine"]
        corresp = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        counters = [Counter(digit) for digit in digits]
        found = [0] * 10
        for it, c in enumerate(counters):
            k = min(cnt[x]//c[x] for x in c)
            for i in c.keys(): c[i] *= k
            cnt -= c
            found[corresp[it]] = k     
        return "".join([str(i) * found[i] for i in range(10)])