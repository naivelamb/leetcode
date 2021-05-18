"""
https://leetcode.com/problems/count-primes/

For each i, mark i * (2,3,4,5,6....) as not prime.
Keep doing this. 

"""
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [1] * n
        i = 2
        while i ** 2 < n:
            if isPrime[i] == 0:
                continue
            j = i ** 2
            while j < n:
                isPrime[j] = 0
                j += i
            i += 1

        return sum(isPrime[2:])