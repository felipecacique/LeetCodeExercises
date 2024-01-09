# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # lets try a modified binary search. We do a logn binary search algorithm to find the pivot index. Then we create aux indexes to to map this array to a non rotated array. We perform a second binary seach using aux indexes.

        # PART-1
        n = len(nums)

        start_rotated_array = 0

        if n > 1 and nums[-1] < nums[0]: # it is a rotated array
            
            # finding the pivot index. Actually we want the start index of this rotated array 
            right = n-1
            left = 0 
            
            while right - left > 1: # the pivor happens to be the right when right - left == 1. Exp: nums = [4,5,6,7,0,1,2] we stop when left is pointing to the number 7, and right is pointing to 0. Left will point to the end the rotated array, and right will point to the beggining of the rotated array
        
                middle = int((left + right)/2)
                
                if nums[middle] > nums[left]: # the pivot is not between middle and left, so it must be in the right side (between middle and right), we update the left = middle
                    left = middle # update left to the middle
            
                else: #if nums[middle] < nums[right]: # the pivot is not between middle and right, so it must be in the left side (between left and middle), we update the right = middle
                    right = middle
                    
            start_rotated_array = right
            end_rotated_array = left
            print(start_rotated_array)


        # PART-2
        # now that we have the new start and end indexes, we do the second binary search to find the target
        def mapIndex(i):
            # imagine we have the original nums, and the sorted_nums (without rotation). This function maps the index i (that corresponds to the imaginary sorted_nums) to the index of the nums, so that sorted_nums[i] = nums[mapIndex(i)]. This way we do not need to actually create a secondary array. W just map one to another.

            return (start_rotated_array + i) % n

        
        right = n-1
        left = 0 
        while left <= right:
            
            middle = int((left + right)/2)
            print(left, right, middle, mapIndex(middle), nums[mapIndex(middle)])

            if nums[mapIndex(middle)] == target:
                return mapIndex(middle)

            if nums[mapIndex(middle)] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1