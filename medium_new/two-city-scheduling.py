class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # https://leetcode.com/problems/two-city-scheduling/
        # economia b - 1: -10, -170, 350, 10. So if we go to a instead of b, we save how many dolars?
        # we create a list with that. Sorte it. And the first 100 goest to a, e the remaining goes to b.
        
        savingsToA = []
        for i, (a, b) in enumerate(costs):
            savingsToA.append((a-b, i))
        
        savingsToA = sorted(savingsToA)
        
        total = 0
        for i in range(len(costs)):
            if i < len(costs)//2:
                # goes to a
                total += costs[savingsToA[i][1]][0]
            else:
                # goes to b
                total += costs[savingsToA[i][1]][1]
        
        return total
        