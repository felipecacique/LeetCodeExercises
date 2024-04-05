class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def Solution1(coins, amount):
            # Solution1: Divide and conquer with dinamic programming. Top-down, it is a brute force solution with memoization. We do solution(coins, amount) = min(solution(coin, amount-largest_coin) for coin in coins) + 1. In other words, the solution for a problem p is the best solution among all p children. And so on. The solution is build during the dfs, in a post order transversal. We will use a harshtable to store the alredy calculated solutions.

            solutions = {}

            # coins = list(reversed(sorted(coins))) # so we can start from the largest coins first

            def solution(amount):
                
                if amount in solutions:
                    return solutions[amount]

                if amount == 0:
                    return 0
                
                if amount < 0:
                    return float('inf')

                # removed_coins = []
                # while coins[-1] > amount: # the coin is not a cancidate since its value is greatter than the amount. So we must remove it from coins list
                #     removed_coins.append(coins.pop())
                #     if len(coins) == 0: # all coins removed, so imposible to solve the problem
                #         break

                min_coins = float('inf')
                
                for coin in coins: # lets start first from the largest coins, so we get to the base cases quicker
                    n_coins = solution(amount-coin)
                    min_coins = min(min_coins,n_coins + 1) # get the best solution of this node's children. We add 1, and that is the best solution of this node.
                    
                
                # for coin in reversed(removed_coins): # put the removes coins back to the list, since we are going to jump to a node up. And thos removed coins here must be included there
                #     coins.append(coin)

                solutions[amount] = min_coins
        
                return min_coins

            
            min_coins = solution(amount)

            if min_coins == float('inf'): 
                return -1
            else:
                return min_coins
            

        def Solution2(coins, amount):
            # got solution from https://www.youtube.com/watch?v=SIHLJdF4F8A&ab_channel=AlgoEngine. dinamic programing bottom-up apporach do not need recursion. It is fasten than solution1 since it does not need to do recursion

            dp = [0] + ([float('inf')] * amount)
            for i in range(1, amount + 1):
                for coin in coins:
                    if coin <= i:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
            
            if dp[-1] == float('inf'):
                return -1
            return dp[-1]


        def Solution3(coins, amount):
            # remaking this problem 4 months latter. Bottom up approach, dynamic programming
            # create an array with the min ammout of coin to reach ith ammount
            # [0, 1, 1, 2, 2, 5]
            dp = [float('inf')] * (amount+1)
            dp[0] = 0 # base case
            for i in range(1, amount+1):
                for coin in coins:
                    if i-coin >= 0:
                        dp[i] = min(dp[i],dp[i-coin]+1)

            return dp[-1] if dp[-1]!= float('inf') else -1


        return Solution2(coins, amount)

