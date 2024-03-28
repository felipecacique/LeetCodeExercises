class Solution:
    # https://leetcode.com/problems/fibonacci-number/
    
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        fib_1 = 1
        fib_2 = 0
        for i in range(2,n+1):
            fib = fib_1 + fib_2
            fib_1, fib_2 = fib, fib_1

        return fib