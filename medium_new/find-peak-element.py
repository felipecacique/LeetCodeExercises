class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-peak-element/?envType=study-plan-v2&envId=leetcode-75

        nums = [float('-inf')] + nums + [float('-inf')]
        left = 1
        right = len(nums) - 2

        while left <= right:

            middle = int((left+right)/2)

            if nums[middle] > nums[middle-1] and nums[middle] > nums[middle+1]: # we found a peak
                return middle - 1

            elif nums[middle] >= nums[middle-1]:# and nums[left] >= nums[left-1]: # slope is ascendent, then peak is on the right side
                left = middle + 1
            
            else: #if nums[middle] >= nums[middle+1]:# and nums[left] >= nums[left-1]: # slope is descent, then peak is on the left side
                right = middle - 1
            
            # else:
            #     left += 1
            
        return 
