class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/
        for i in range(k):
            minVal = min(nums)
            for i in range(len(nums)):
                if nums[i] == minVal: 
                    nums[i] = nums[i] * multiplier
                    break
        return nums