class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        # https://leetcode.com/problems/minimum-cost-to-set-cooking-time/description/
        digits = 100*(targetSeconds//60) + targetSeconds%60
        
        digits2 = digits
        if digits%100 == 0 and digits//100 > 0:
            digits2 = digits - 100 + 60
        
        digits3 = digits
        if targetSeconds > 60 and targetSeconds%60 < 40:
            digits3 = (digits // 100 - 1)*100 + 60 + targetSeconds%60
            

        def getMinCost(digits):
            digits = str(digits)
            if len(digits) > 4: return float("inf")
            cost= 0
            prev = None
            for i, d in enumerate(digits):
                if i == 0 and d == str(startAt):
                    cost += pushCost
                elif prev and d == prev:
                    cost += pushCost
                else:
                    cost += moveCost + pushCost
                prev = d
            return cost
        
        return min(getMinCost(digits), getMinCost(digits2), getMinCost(digits3))