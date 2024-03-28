class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # combinatorial problem - backtracking
        # https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
        
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