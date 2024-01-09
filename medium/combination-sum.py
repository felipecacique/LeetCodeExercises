# https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # this problem seems the min-coin-problem, but in this case we but return all the combinations ... 
        # also seems the problems of 2-sum and 3-sum ..... more like an n-sum. 
        # i will try something similar ro the coin problem, "brute force", iterative version built it from buttom up

        # The idea here will be computing all combinations, but avoinding computing the same combination mode then once, because this is what explodes the time complexity. Exp: [2,3] and [3,2]. Lets say candidates = [c1, c2, c3 ... cn]. Lets find a way to crete all the combinations with the c1 always appearing in the left of c2, and c2 on the left of c3 and so on. We startr with a combinations = [(0,[])], tuple holding the sum and the combination that leads to that sum. Since the combination is empty list, the sum is 0. For the candidate c1, we will get all combinations in the list and crete all the possible solutions using c1, adding c1 one by one until the sum is greatter than the target. Example. In the loop 0: combinations = [(0,[])], loop 1: combinations = [(0,[]),(c1,[c1])], loop n: combinations = [(0,[]),(c1,[c1]) ... (c1*n,[c1, c1, c1 ... ])]. In other words we will have all combinations where c1 does not appear, where c1 appears once, where c1 appears twice, ... Note that we are building our solution bit by bit. After that we do the same for the second candidate c2. For each combination in the list, we add c2 1 time, c2 2 time, c2 3 times ..., always computing the sum, until the sum > target. Now there will be solutions such as [], [c1], [c1, c1], [c2], [c1, c2], [c1, c2, c2], [c1, c1, c2], [c1, c1, c2, c2] ... We repeat this process for all candidates. In the end we get all combinations where the sum == target, and that is our solution. In symary we are building all combinations avoiding redudancy. With this approach we will only have combinations where c1 appears before c2, and so on. 47ms Beats 95.92%of users with Python3. time O(target^candidate). 

        def Solution1(candidates, target):
            
            output = []
            combinations = [(0,[])] # hold the sum and the combination pairs

            for candidate in candidates: 

                for i in range(0,len(combinations)): # for each combination already created
                    combination = combinations[i]
                    
                    while True: # build new combinations by adding the candidate ck once, twice ... untill the sum > target
                        new_sum = combination[0] + candidate
                        if new_sum > target:
                            break

                        new_combination = combination[1].copy()
                        new_combination.append(candidate)

                        combinations.append( (new_sum, new_combination) )
                        combination = combinations[-1] # points to the last combination that we have just created. If we have just added ck, in the next loop it will do a copy of it and add another ck, creating a new combination, and so on.

            for combination in combinations: # get all combinations with sum == target
                if combination[0] == target:
                    output.append( combination[1] )

            return output
        
        return Solution1(candidates, target)
