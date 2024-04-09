class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/?envType=study-plan-v2&envId=top-interview-150
        # same approach as Best Time to Buy and Sell Stock III but intead of 2 windoes only, we must make it generic wihth all windows interval. O(n^2)

        if len(prices) == 1: return 0

        diffs = [0]+[prices[i] - prices[i-1] for i in range(1,len(prices))]
        maxArrTo = [[0] * len(diffs) for _ in range(k+1)]

        # calculate the max sequence from 0 to i
        for j in range(1,k+1):
            max_sequence = 0
            global_max = 0
            for i in range(1,len(diffs)):
                if max_sequence + diffs[i] > diffs[i] + maxArrTo[j-1][i-1]:
                    max_sequence =  max_sequence + diffs[i]
                else: 
                    max_sequence = diffs[i] + maxArrTo[j-1][i-1]
                global_max = max(global_max, max_sequence)
                maxArrTo[j][i] = global_max
        
        return maxArrTo[-1][-1]