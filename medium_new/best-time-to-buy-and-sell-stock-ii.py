class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/1227085439/?envType=study-plan-v2&envId=top-interview-150
        diff_pos = []
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1] > 0:
                diff_pos.append(prices[i]-prices[i-1])
        return sum(diff_pos)