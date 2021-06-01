"""
https://leetcode.com/problems/search-suggestions-system/

Sort the products, binary search the position of the prefix, check the next 3 product. 

Time complexity: O(mlogn)
m = len(searchWord)
n = len(products)
"""
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res, prefix, i = [], '', 0
        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix, i)
            res.append([w for w in products[i:i+3] if w.startswith(prefix)])
        return res