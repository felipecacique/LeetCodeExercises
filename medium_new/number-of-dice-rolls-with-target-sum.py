class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # combinatorial problem
        # https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
        
        def Solution1():
            # top-down approach: backtracking and dp

            MOD = 10**9 + 7
            combinations = [1]
            hashtable = {}
            
            
            def bfs(dice,target):
                if dice == 0 and target == 0: return 1
                if dice == 0: return 0
                
                if (dice, target) in hashtable:
                    return hashtable[ (dice, target) ]
                
                total_combinations = 0
                for num in range(1,k+1):
                    if target-num < 0:
                        break
                        
                    total_combinations = ( total_combinations + bfs(dice-1, target-num) ) 
                    
                hashtable[ (dice, target) ] = total_combinations
                    
                return total_combinations
                
            total_combinations = bfs(n,target)
            
            return total_combinations % MOD
        


        def Solution2():
            # using for loops and dp - n, k, target

            MOD = 10**9 + 7
            
            # dp = [[0] * n for _ in k]
            dp = { (0,0):0 } # (sum, k) stores the number of combinations
            prev_sum = [0] * (k+1)
            
            combs = [[0,0]]
            for i in range(1, n+1): # play the dices n times
                new_combs = []
                for num in range(1,k+1): # play the ith dice
                    # for all previous combinations of size ith-1, add the new dice
                    for comb in combs:
                        if (i<n and comb[1]+num < target) or (i==n and comb[1]+num == target):
                            new_comb = [ comb[1]+num, i]
                            new_combs.append(new_comb)
                            # dp[ comb[1]+num, i] = dp[ comb[1], i-1] + 1

                combs = new_combs   
        
            return len(combs) % MOD


        def Solution3():
            # bottom up approach. Instead of usig tree, wee will built the simple solutions first and use the previous ons to build the next, and so on untill in our solution. Eg. If we throw 1 dice n=1 , how many possibilities to reach count = 1, 2, 3 ... We thow thr second dice n=2,   how many possibilities to reach count = 1, 2, 3 .. But to know these possibilies que can just look at the  previous row n=1. The combinations to reach a target = 4 using 2 dices is the sum of the combination of comb(n=1,target=1)+comb(n=1,target=2)+comb(n=1,target=3) (already in the table)

            MOD = 10**9 + 7
            
            dp = [[0] * (target+1) for _ in range(n+1)] # It will be used to count the combinations. The key is the target and n
            dp[0][0] = 1 # it is our base case, that simplify the solution

            for i in range(1, n+1): # play the dices n times
                for t in range(1,target+1):
                    for x in range(max(0,t-k),t): # count the row ith-1 and where <t
                        dp[i][t] = (dp[i][t] + dp[i-1][x]) % MOD

            return dp[n][target] 
        
        return Solution3()


# class Solution:
#     def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
#         MOD = 10**9 + 7
        
#         dp = [{} for _ in range(n+1)]
#         dp[0][0] = 1
#         for dice in range(1, n+1):
#             for sum_, count in dp[dice-1].items():
#                 for face in range(1, k+1):
#                     if sum_ + face > target:
#                         continue
#                     dp[dice][sum_ + face] = (dp[dice].get(sum_ + face, 0) + count) % MOD

#         return dp[n][target] if target in dp[n] else 0