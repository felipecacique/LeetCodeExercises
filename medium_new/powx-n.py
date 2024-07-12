class Solution:
    def myPow(self, x: float, n: int) -> float:
        # https://leetcode.com/problems/powx-n/submissions/1318814880/?envType=study-plan-v2&envId=top-interview-150
        #
        # works but too slow 
        # p = 1
        # for i in range(abs(n)):
        #     p *= x
        # if n<0: p = 1/p
        
        # return p

        memo = {0:1, 1:x}
        def myPow(n):
            if n in memo: return memo[n]
            c = n//2
            a = myPow(c)
            b = myPow(n-c)
            m = a*b
            memo[n] = m
            return m
        p = myPow(abs(n))
        if n<0: p = 1/p
        return p
