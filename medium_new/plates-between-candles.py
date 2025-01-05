class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # https://leetcode.com/problems/plates-between-candles/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
        # O(nlogn). There is another solution that is better - linear. No need to do binary search. Just create another array of size s with the index of the closest candle in a cumSum fashion
        # create an array with the candle indexes
        
        # candleIndex = []
        # for i in range(len(s)):
        #     if s[i] == "|": candleIndex.append(i)
        
        # # Use binary search to find de closest candle to the left, and the closest to the right (within the interval). 
        # def GetFirstCandleWithinInterval(intervalLeft):
        # # Lets find the left candle. Find the leftmost insertion point
        #     l, r = 0, len(candleIndex) - 1
        #     while l < r:
        #         m = (l+r)//2
        #         if candleIndex[m] < intervalLeft:
        #             l = m + 1
        #         else:
        #             r = m
        #     return l

        # ans = [0] * len(queries)
        # for j, (left, right) in enumerate(queries):
        #     firstCandleInS = GetFirstCandleWithinInterval(left) # get the the first candle in the right
        #     lastCandleInS_ = GetFirstCandleWithinInterval(right) # get the the first candle in the right
        #     lastCandleInS = lastCandleInS_ if lastCandleInS_ < len(candleIndex) and candleIndex[lastCandleInS_] <= right else lastCandleInS_- 1 # transform it to be the first candle in the left
        #     if (firstCandleInS < len(candleIndex) and candleIndex[firstCandleInS] >= left and candleIndex[firstCandleInS] <= right) and (lastCandleInS > 0 and (candleIndex[lastCandleInS] >= left and candleIndex[lastCandleInS] <= right)) and candleIndex[lastCandleInS] != candleIndex[firstCandleInS]:
        #         # Both candles are within the interval, so the interval there at least 2 candles. So lets calculate the number of plates between
        #         candles = lastCandleInS - firstCandleInS + 1
        #         total = candleIndex[lastCandleInS] - candleIndex[firstCandleInS] + 1
        #         plates = total - candles
        #         ans[j] = plates

        # return ans
        

        # O(n)
        closestFromLeft = [float('-inf')] * len(s)
        for i in range(len(s)):
            if s[i] == "|": closestFromLeft[i] = i
            elif i-1 >= 0: closestFromLeft[i] = closestFromLeft[i-1]

        closestFromRight = [float('inf')] * len(s)
        for i in range(len(s)-1, -1, -1):
            if s[i] == "|": closestFromRight[i] = i
            elif i+1 < len(s): closestFromRight[i] = closestFromRight[i+1]
        
        cumSumFromLeft = [0] * len(s)
        for i in range(len(s)):
            if i == 0:
                if s[i] == "*": cumSumFromLeft[i] = 1
                continue
            if s[i] == "*": cumSumFromLeft[i] = cumSumFromLeft[i-1] + 1
            else: cumSumFromLeft[i] = cumSumFromLeft[i-1]

        ans = [0] * len(queries)
        for j, (left, right) in enumerate(queries):
            firstCandleInS = closestFromRight[left]
            lastCandleInS = closestFromLeft[right] 
            if not (lastCandleInS < left or firstCandleInS > right):
            # if (firstCandleInS >= left and firstCandleInS <= right) and (lastCandleInS >= left and lastCandleInS <= right) and lastCandleInS != firstCandleInS:
                # Both candles are within the interval, so the interval there at least 2 candles. So lets calculate the number of plates between
                ans[j] = cumSumFromLeft[lastCandleInS] - cumSumFromLeft[firstCandleInS] 

        return ans

