class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left+right)//2
            if nums[middle] < nums[right]: right = middle
            else: left = middle + 1
        return nums[middle]
    

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         # binary search
#         left = 0
#         right = len(nums) - 1
#         output = float("inf")
#         while left <= right:
#             middle = (left+right)//2
#             if nums[right] < nums[left]:
#                 if nums[middle] > nums[left]: left = middle + 1 # min is on the right side
#                 else: right = middle - 1
#             else: # nums[right] >= nums[left] the logic now is the oposite
#                 if nums[middle] < nums[left]: left = middle + 1 # min is on the left side
#                 else: right = middle - 1
#             output = min(output, nums[middle], nums[right], nums[left])
#         return output