class Solution:
    def trailingZeroes(self, n: int) -> int:
        # https://leetcode.com/problems/factorial-trailing-zeroes/?envType=study-plan-v2&envId=top-interview-150
        # if n == 0:
        #     return 0 

        fac = 1
        count = 0
        count5 = 0
        count2 = 0
        for i in range(1, n+1):
            while i % 5 == 0:
                i //= 5
                count5 += 1
            # while i % 2 == 0:
            #     i //= 2
            #     count2 += 1
            # while i % 10 == 0:
            #     i //= 10
            #     count += 1

            # fac *= i

    
        return count5
        # return count + min(count2, count5)
            


        