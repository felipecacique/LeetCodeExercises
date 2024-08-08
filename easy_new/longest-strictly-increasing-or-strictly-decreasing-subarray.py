class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/submissions/1349091635/
        s = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                s[i] = s[i-1] + 1
        

        r = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                r[i] = r[i-1] + 1
        
        return max(max(r), max(s))
            