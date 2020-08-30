"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge/553/week-5-august-29th-august-31st/3442/

Union-Find, the union is marked by common factors.
For each number, do prime decompsition, get all its prime facotrs.
When build Union-Find, union all numbers belong to the same prime factor.
At last count size of each union, find the maximum one.


"""
class DSU:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.rank[px] += 1

class Solution:
    def primeDecompose(self, n): # time complexity: O(sqrt(n))
        prime_factors = set()
        while n % 2 == 0:
            prime_factors.add(2)
            n //= 2

        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                prime_factors.add(i)
                n //= i

        if n > 2:
            prime_factors.add(n)
        return prime_factors

    def largestComponentSize(self, A: List[int]) -> int:
        # build divisor map
        idx_map = {A[i] for i in range(len(A))}
        dsu = DSU(len(A))
        num_factor_map = collections.defaultdict(set)
        for i, n in enumerate(A):
            prime_factors = self.primeDecompose(n) # num of prime factors' upper bond would be log2(M), M = max(A)
            for f in prime_factors:
                num_factor_map[f].add(i)

        # build the union find
        for d, indices in num_factor_map.items():
            indices = list(indices)
            if indices:
                root = indices[0]
                for node in indices[1:]:
                    dsu.union(root, node)
        # get answer
        res = {}
        ans = 0
        for i in range(len(A)):
            res[dsu.find(i)] = res.get(dsu.find(i), 0) + 1
            ans = max(ans, res[dsu.find(i)])
        return ans
