class Solution:
    def candy(self, ratings: List[int]) -> int:
        # https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150
        # based on the neetcode's solution on https://www.youtube.com/watch?v=1IzCRCcK17A
        
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i+1] + 1, candies[i])
        
        return sum(candies)



        # total = 1
        # lastCandy = 1
        # prevPeakDown = 0
        # lastPeakHigh = 0
        # for i in range(1, len(ratings)):
        #     if lastCandy >= 1 and ratings[i] > ratings[i-1]:
        #         lastCandy += 1
        #         lastPeakHigh = i
        #     elif lastCandy > 1 or ratings[i] == ratings[i-1]: # ratings[i] <= ratings[i-1]
        #         lastCandy = 1
        #         prevPeakDown = i
        #     else: #ratings[i] <= ratings[i-1] and lastCandy <= 1
        #         total += (i - prevPeakDown)
        #         total += 1 if i - prevPeakDown > ratings[lastPeakHigh] - ratings[prevPeakDown] - 1 else 0
        #         lastCandy = 1
        #     total += lastCandy
            
        # return total
