class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        # https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/
        # this is similar to the coin-change problem, but instead having to find the minimum number of coins that add up to target, we need to fing the largest number of "coins"
        
        def Solution1(nums,target):
            # create an array with the max ammout of coin to reach ith ammount
            # [0, 1, 2, 3, 4, 5]
            if sum(nums) < target:
                return -1

            nums = sorted(nums) # this solves tr problem of reaching a 1 to target with more than one possibilities. But idk why ... 
            
            dp = [ [float('-inf'), set()] for _ in range(target+1) ] 
            dp[0] = [0,set([i for i in range(len(nums))])] # base case
            for i in range(0, target+1):
                for j, num in enumerate(nums):
                    if i-num < 0: continue
                    if j in dp[i-num][1]: # if the number num is yet available
                        if dp[i-num][0]+1 > dp[i][0]: # get the longgest sequence that num can be added
                            # notice that there may be more than one dp[i-num][0]+1 that leads to the same number, in other words, there might be many possibilities ... Since we sorted our nums, it neems that we dont need to take acoount for all possibiliteis, but just get the first one. It worked fine this way ... but a still dont know why sorting nums could solve the problem ...
                            dp[i][0] = dp[i-num][0]+1
                            dp[i][1] = dp[i-num][1].copy()
                            dp[i][1].remove(j) # since we used num to jump from i-num to i, then we must remove the number num from the set. ith will hold the longgest subsequence len so far and a set with all numbers it can is till use from it
            return dp[-1][0] if dp[-1][0] != float('-inf') else -1


        def Solution2(nums,target):
            # inspired by a submission's solution, but instead of muving backwards, i am moving forward. An also using dictionary insteado of an array of size target
            dp = {0:0, target:-1}
            nums = nums
            for num in nums:
                dpCopy = dp.copy()
                for t, count in dpCopy.items():
                    if t+num <= target:
                        dp[t+num] = max(dpCopy.get(t+num,-1), dpCopy[t] + 1) 
            return dp[target]


        def Solution3(nums,target):
            # moving backward, inspided by a submission's solution
            dp = [0] + [-1 for _ in range(target)] 
            for num in nums:
                for i in range(len(dp)-1-num,-1,-1):
                    if dp[i] >= 0:
                        dp[i+num] = max(dp[i+num], dp[i]+1)            
            return dp[target]

        return Solution3(nums,target)