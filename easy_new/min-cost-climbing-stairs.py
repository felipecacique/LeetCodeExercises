class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # https://leetcode.com/problems/min-cost-climbing-stairs/?envType=study-plan-v2&envId=leetcode-75
        # use dinamic programming, array. Where we save the best cost for that specific step based on the cost of the lat two steps

        # minCostArr = [cost[0], cost[1]]

        # for i in range(2,len(cost)):
        #     minCostArr.append(min(minCostArr[-1], minCostArr[-2])+cost[i])
   
        # return min(minCostArr[-1], minCostArr[-2])

        a, b = cost[0], cost[1]

        for i in range(2,len(cost)):
            c = min(a, b)+cost[i]
            a = b
            b = c
   
        return min(a, b)