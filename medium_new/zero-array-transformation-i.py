class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # https://leetcode.com/problems/zero-array-transformation-i/description/
        # O(m+n)
        dp = [0] * len(nums)
        for l, r in queries:
            if l < len(dp): dp[l] += 1
            if r+1 < len(dp): dp[r+1] -= 1

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
            