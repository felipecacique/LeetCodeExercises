class Solution:
    def countPrimes(self, n: int) -> int:
        # https://leetcode.com/problems/count-primes/
        if n <= 2: return 0

        # this solution is slow but works
        # primes = [2]
        # def is_prime(num):
        #     for p in primes:
        #         if num % p == 0: return # num is divisible by p, so it is not prime
        #     primes.append(num)
        #     return
           
        # for num in range(2,n):
        #     is_prime(num)

        # return len(primes)

        # inspired from https://www.youtube.com/watch?v=R6zyD06Yn3k
        is_prime = [True]*n
        is_prime[0] = is_prime[1] = False
        for i in range(2,n):
            if is_prime[i]:
                j = i + i
                while j < n:
                    is_prime[j] = False
                    j += i
            
        return sum(is_prime)


        