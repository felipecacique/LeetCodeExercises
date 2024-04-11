class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # https://leetcode.com/problems/new-21-game/
        # we will use an approach similar to the coin-change problem
        def Solution1(n,k,maxPts):
            dp = [1] + [0] * (max(n, k+maxPts))
            for i in range(k):
                for card in range(1,maxPts+1):
                    # dp[i+card] = dp[i+card] + dp[i]
                    dp[i+card] = dp[i+card] + dp[i] / maxPts
            return sum(dp[k:n+1]) / sum(dp[k:])

        # def Solution2(n,k,maxPts):
        #     dp = [0] + [0] * (max(n, k+maxPts-1))
        #     for i in range(1,len(dp)):
        #         if i > maxPts:
        #             dp[i] = (dp[min(i-1,k)] - dp[i-maxPts]/maxPts)  +  dp[i-1]/maxPts
        #         else: 
        #             dp[i] = dp[i-1]/maxPts + 1/maxPts
        #     print(dp)
        #     return sum(dp[k:n+1]) / sum(dp[k:])

        # def Solution2(n,k,maxPts):
        #     dp = [0] * (max(n, k+maxPts+1))
        #     for i in range(1,len(dp)): 
        #         dp[i] = (1/maxPts)*dp[min(i-1,k-1)] #+ dp[min(i-1,k)]  - dp[max(0,min(i-maxPts,k))]
        #         if i <= maxPts:
        #             dp[i] = dp[i] + 1 / maxPts
        #     print(dp)
        #     return sum(dp[k:n+1]) / sum(dp[k:])

        def Solution2(n,k,maxPts):
            dp = [0] + [1/maxPts] * (max(n, k+maxPts))
            for i in range(2,len(dp)): 
                # dp[i] = (1/maxPts)*dp[min(i-1,k-1)] #+ dp[min(i-1,k)]  - dp[max(0,min(i-maxPts,k))]
                j = min(i,k)
                if i <= maxPts:
                    dp[i] = dp[j-1] + dp[j-1] / maxPts
                else: #if i-maxPts >= k  :
                    dp[i] = dp[j-1] + dp[j-1] / maxPts - dp[i-maxPts]
            print(dp)
            return sum(dp[k:n+1]) / sum(dp[k:])
        return Solution2(n,k,maxPts)
