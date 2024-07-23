class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/?envType=study-plan-v2&envId=leetcode-75

        totalProfit = 0
        profit = 0
        maxProfit = 0
        prices.append(float("-inf"))
        for i in range(1, len(prices)):
            profit += prices[i] - prices[i-1]
            maxProfit = max(maxProfit, profit)
            # Find the close position
            if profit - maxProfit <= -fee : # close pos at the maxProfit if the consecutive loss (draw down) >= fee. In this case we could just have close the position at the max and opened a new position right now with the same total profit.
                totalProfit += max(maxProfit-fee, 0) 
                profit, maxProfit = 0, 0 
            # Find the buy position
            if profit <= 0:
                profit, maxProfit = 0, 0 # we have a new start

        return totalProfit

            