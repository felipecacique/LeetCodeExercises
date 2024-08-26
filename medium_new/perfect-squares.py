class Solution:
    def numSquares(self, n: int) -> int:
        # https://leetcode.com/problems/perfect-squares/?envType=study-plan-v2&envId=top-100-liked
        # time o(n**2) or o(n*squares) or o(n*100) space o(n)
        squares = []
        for i in range(1,n+1):
            squares.append(i*i)

        dp = [0] * (n+1)
        for s in squares:  
            for i in range(s ,len(dp)):
                if dp[i] == 0: dp[i] = dp[i-s] + 1
                else: dp[i] = min(dp[i-s] + 1, dp[i])    

        return dp[-1]


# class Solution:
#     def numSquares(self, n: int) -> int:
        
#         squares = []
#         for i in range(1,n+1):
#             squares.append(i*i)

#         dp = [0] * (n+1)
#         squares = squares[::-1]
#         starts = set([0])
#         for s in squares:  
#             for start in starts.copy():
#                 for i in range(start+s, len(dp), s):
#                     if dp[i] == 0: dp[i] = dp[i-s] + 1
#                     else: dp[i] = min(dp[i-s] + 1, dp[i])
#                     starts.add(i)    

#         return dp[-1]