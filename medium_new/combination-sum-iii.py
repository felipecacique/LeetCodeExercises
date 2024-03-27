class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # https://leetcode.com/problems/combination-sum-iii/submissions/1214979732/?envType=study-plan-v2&envId=leetcode-75
        
        solution = set()
        combinations = [[[num],num,1] for num in range(1,10)] # ([],0,0) # holds combination and its sum and the ammount of numbers
        for i in range(k-1):
            new_combs = []
            for num in range(1+i,10):
                for combination in combinations:
                    if combination[2] < k and combination[1] + num <= n and not num in combination[0]:
                        new_comb = [combination[0].copy(), combination[1], combination[2]]
                        new_comb[0].append(num)
                        new_comb[1] += num
                        new_comb[2] += 1
                        if new_comb[2] == k and new_comb[1] == n:
                            solution.add(tuple(sorted(new_comb[0])))
                        new_combs.append(new_comb)
            combinations = new_combs
        return solution

                
