class Solution:
    def minOperations(self, k: int) -> int:
        # https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/
        # add + dup
        # (1*add) * dup = k
        # add and dup must be the closest as possible
        # k / dup = add
        # so add*dup =k and add = dup ideally. Thus dup*dup = k, add = dup = sqrt(k). So min operations is add + dup that is 2*sqrt(k). Is is close to it.
        import math
        dup = math.floor(k**0.5)
        add = math.ceil(k**0.5) 
        # print(dup, add, k**0.5)
        # sol = dup + add - 2 # we decrease 2 because the inicial array has already one element with value 1. So 1 operation of add1 and "double" already
        
        sol = dup + add
        if dup * add >= k: sol = min(sol, dup + add - 2)
        if (dup+1) * add >= k: sol = min(sol, dup + 1 + add - 2)
        if dup * (add+1) >= k: sol = min(sol, dup + add + 1 - 2)
        
        return sol
