class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/reach-end-of-array-with-max-score/description/
        # o(n)
        maxVal = 0
        sol = 0
        for i in range(len(nums)-1):
            maxVal = max(maxVal, nums[i])
            sol += maxVal
        
        return sol