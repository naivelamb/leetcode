"""
https://leetcode.com/problems/remove-9/
"""
class Solution:
    def newInteger(self, n: int) -> int:
        if n < 9:
            return n

        mem = {}
        def count9(num):
            if num in mem:
                return mem[num]
            N = len(num)
            if N == 0 or num == '0':
                return 0
            c = num[0]
            d = int(c)
            ans = d * count9(str(10**(N-1) - 1))
            if c == '9':
                ans += 1
                if N > 1:
                    ans += int(num[1:])
            else:
                ans += count9(num[1:])
            mem[num] = ans
            return ans

        p, q = n, 2*n

        def cleanup(n):
            # remove all numbers contains 9
            num = str(n)
            for i in range(len(num)):
                if num[i] == '9':
                    ans = num[:i] + ('8' * len(num[i:]))
                    return int(ans)
            return n

        while True:
            cnt = count9(str(q))
            cnt = q - cnt
            #print mem
            #print q, cnt
            if cnt == n:
                return cleanup(q)
            elif cnt < n:
                p = q
                q *= 2
            else:
                break
        #print "here"
        while p < q:
            mid = p + (q-p)//2
            cnt = count9(str(mid))
            cnt = mid - cnt
            #print mem
            #print mid, cnt
            if cnt == n:
                return cleanup(mid)
            elif cnt < n:
                p = mid + 1
            else:
                q = mid - 1
        return cleanup(p)


sol = Solution()
n = 9
assert sol.newInteger(n) == 10
