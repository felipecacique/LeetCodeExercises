class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # https://leetcode.com/problems/search-insert-position/?envType=study-plan-v2&envId=top-interview-150
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
    
        if target <= nums[left]: return left
        else: return left + 1
