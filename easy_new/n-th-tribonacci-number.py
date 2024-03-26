class Solution:
    def tribonacci(self, n: int) -> int:
        # https://leetcode.com/problems/n-th-tribonacci-number/submissions/1214057762/?envType=study-plan-v2&envId=leetcode-75

        hash = {0:0, 1:1, 2:1}

        def Tribonacci(n):
            return hash[n-1] + hash[n-2] + hash[n-3]
        
        for x in range(0, n+1):
            if not x in hash:
                hash[x] = Tribonacci(x)
        
        return hash[n]