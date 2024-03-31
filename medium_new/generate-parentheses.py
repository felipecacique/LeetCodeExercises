class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # https://leetcode.com/problems/generate-parentheses/
        
        combs = [([],0, 0)]
        
        for i in range(2*n):
            new_combs = []
            for comb in combs:
                
                for c in [1,-1]: # 1 represents "(" and -1 ")"
                    
                    if c == -1 and comb[2] >= 1: # represents the sum 
                        comb_copy = comb[0][:] + [")"]
                        count1 = comb[1]
                        sumArr = comb[2]
                        new_combs.append( (comb_copy, count1, sumArr-1))

                    if c == 1 and comb[1] < n: # represents the ammount of "("
                        comb_copy = comb[0][:] + ["("]
                        count1 = comb[1]
                        sumArr = comb[2]
                        new_combs.append( (comb_copy, count1+1, sumArr+1))
                        
            combs = new_combs
            
        a = ["".join(comb[0]) for comb in combs]

        return a