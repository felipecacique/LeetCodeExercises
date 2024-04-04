class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
        # use pointers
        if sum(nums) < target: return 0
        start = 0
        minLen = float("inf")
        subSum = 0
        for end in range(len(nums)):
            subSum += nums[end]
            if subSum >= target: 
                while subSum - nums[start] >= target:
                    subSum -= nums[start]
                    start += 1
                minLen = min(minLen, end-start+1)
        return minLen if minLen != float("inf") else 0