"""
https://leetcode.com/problems/decoded-string-at-index/

#1 Simulation. 
Building tape takes too long. 

#2
Use N to keep the length of decoded string, keep decode untill N >= K.
Then we go backward from the decoded position.
If S[i] = d is a digit, N = N // d, K = K % N
If S[i] = c is a character, we return c if K == N or K == 0

"""
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        N = 0
        for i, c in enumerate(S):
            if c.isdigit():
                N *= int(c)
            else:
                N += 1
            if N >= K:
                break
        
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                N //= int(c)
                K %= N
            else:
                if K == 0 or K == N:
                    return c
                else:
                    N -= 1

    def decodeAtIndex_simulation(self, S, K):
        tape = ''
        i, curr_len = 0, 0
        while i < len(S):
            if S[i].isdigit():
                num = int(S[i])
                if curr_len * num >= K:
                    # find ans
                    K %= curr_len
                    return tape[K - 1]
                else:
                    tape *= num
                    curr_len *= num
            else:
                tape += S[i]
                curr_len += 1
                if curr_len == K:
                    return tape[-1]
            i += 1