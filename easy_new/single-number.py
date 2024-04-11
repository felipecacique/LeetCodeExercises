class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/single-number/?envType=study-plan-v2&envId=top-interview-150
        
        ans = nums[0]
        for i in range(1,len(nums)):
            ans = ans ^ nums[i]
        return ans