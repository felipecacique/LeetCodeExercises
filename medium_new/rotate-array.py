class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
        nums[:] = nums[len(nums)-k%len(nums):] + nums[0:len(nums)-k%len(nums)]
    