class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # https://leetcode.com/problems/zero-array-transformation-ii/
        # similar to Zero Array Transformation I. We would have to iterate checkSolution k times, however we can use binary search and reduce it to log(n) itereations
        # O((m+n)*logn)

        if sum(nums) == 0: return 0

        def checkSolution(k):
            dp = [0] * len(nums)
            for l, r, val in queries[:k+1]:
                if l < len(dp): dp[l] += val
                if r+1 < len(dp): dp[r+1] -= val

            # do a cum sum
            cumSum = [0] * len(nums)
            for i in range(len(dp)):
                if i == 0:
                    cumSum[i] = dp[i]
                    continue
                cumSum[i] = cumSum[i-1] + dp[i]

            for i in range(len(nums)):
                if cumSum[i] - nums[i] < 0:
                    return False
            return True
        
        # binary search
        left = 0
        right = len(queries) - 1
        while left < right:
            mid = (left + right) // 2
            if checkSolution(mid) == True:
                right = mid
            else:
                left = mid + 1

        return left + 1 if checkSolution(left) else -1


        # if sum(nums) == 0: return 0
        # ans = 0

        # queries = [ (r, k, l, val)  for k, (l, r, val) in enumerate(queries) ]
        # queries.sort()

        # def binarySearch(queries, i):
        #     left = 0
        #     right = len(queries) - 1
        #     while left < right:
        #         mid = (left + right) // 2
        #         l, k, r, val = queries[mid]
        #         if queries[mid][0] >= i:
        #             right = mid
        #         else:
        #             left = mid + 1
        #     return left
        
        # for i in range(len(nums)):
        #     # find the start point by binary search
        #     # start = binarySearch(queries, i)
        #     start = 0
        #     for j in range(start,len(queries)): # just go over the promissing intervals instead of all
        #         print(i, j, queries[j], "   ", nums)
        #         r, k, l, val = queries[j]
        #         # if l > i: break # stop iteraction since the next intervals start after the index i, so we can skip them all
        #         if i >= l and i <= r: nums[i] = max(0, nums[i] - val)
        #         if nums[i] == 0:
        #             ans = max(ans, k+1)
        #             break
                   
        #     if nums[i] > 0: return -1
            
        # return ans

        


        # if sum(nums) == 0: return 0
        # ans = 0
        # for i in range(len(nums)):
        #     for k, (l, r, val) in enumerate(queries):
        #         if i >= l and i <= r: nums[i] = max(0, nums[i] - val)
        #         if nums[i] == 0:
        #             ans = max(ans, k+1)
        #             break
                    
        #     if nums[i] > 0: return -1
            
        # return ans
        

        #         if sum(nums) == 0: return 0
            
        # for k, (l, r, val) in enumerate(queries):
            
        #     for i in range(l, r+1):
        #         if i < len(nums): nums[i] = max(0, nums[i] - val)

        #     if sum(nums) == 0:
        #         return k + 1
                
        # return -1

