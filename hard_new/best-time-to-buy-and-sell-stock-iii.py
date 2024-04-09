class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/?envType=study-plan-v2&envId=top-interview-150
        # find the 2 subsequences with max sum will not work
        # programacao dinamica

        if len(prices) == 1: return 0

        diffs = [prices[i] - prices[i-1] for i in range(1,len(prices))]
        maxArrTo = [0] * len(diffs)
        maxArrFrom = [0] * len(diffs)

        # calculate the max sequence from 0 to i
        max_sequence = 0
        global_max = 0
        for i in range(len(diffs)):
            if max_sequence + diffs[i] > diffs[i]:
                max_sequence =  max_sequence + diffs[i]
            else: 
                max_sequence = diffs[i]
            global_max = max(global_max, max_sequence)
            maxArrTo[i] = global_max
        
        # repeat the process backwards. We want to get the max, but since we are doing it backwards, we must get the min and invert the signal
        min_sequence = 0
        global_max = 0
        for i in range(len(diffs)-1,-1,-1):
            if min_sequence + -diffs[i] < -diffs[i]:
                min_sequence =  min_sequence + -diffs[i]
            else: 
                min_sequence = -diffs[i]
            global_max = max(global_max, -min_sequence) 
            maxArrFrom[i] = global_max
        
        # the profit is the sum of the sequence from 0 to i and the sequence i+1 to n. Then we return the max of those profits
        max_profit = 0
        for i in range(len(maxArrTo)):
            if i+1 < len(maxArrTo): profit = maxArrTo[i] + maxArrFrom[i+1]
            else: profit = maxArrTo[i]
            max_profit = max(max_profit, profit)
        
        return max_profit
