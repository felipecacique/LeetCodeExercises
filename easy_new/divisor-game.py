class Solution:
    def divisorGame(self, n: int) -> bool:
        # https://leetcode.com/problems/divisor-game/description/
        # 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        # n = 4
        
#         def dfs(player,x1, x2, n):
            
#             # player loses
#             if player == 1 and x1 >= n and x1 % n != 0: return -1    # alice, bob
#             if player == -1 and x2 >= n and x2 % n != 0: return 1   # alice, bob
            
#             # the best choince of player A is the one that leads 
#             countMax = -1
#             countMin = float('inf')
#             for x in range(1,n):
#                 # if n - x > 0:
#                 if player == 1: # wants to take the best choice that maximizes player 1 score
#                     countPlayer1 = dfs(player*-1, x, x2, n-x)
#                     countMax = max(countMax, countPlayer1)
#                 if player == -1: # wants to take the best choice that minimizes player 1 score
#                     countPlayer1 = dfs(player*-1, x1, x, n-x)    
#                     countMin = min(countMin, countPlayer1)
#             countMinMax = countMax if player == 1 else countMin 
#             return countMinMax
        
#         countMinMax = dfs(1,0,0, n)
        
#         if countMinMax > 0:
#             return True # alice wins
#         else:
#             return False
        
        if n % 2 == 0: return True
        else:
            return False