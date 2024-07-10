class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # https://leetcode.com/problems/summary-ranges/?envType=study-plan-v2&envId=top-interview-150
        output = []
        for i, num in enumerate(nums):
            if i == 0 or nums[i] - nums[i-1] > 1:
                start = nums[i]
            if i+1 >= len(nums) or nums[i+1] - nums[i] > 1:
                end = nums[i]
                if start == end: output.append(str(start))
                else: output.append(str(start)+"->"+str(end))
        return output