# https://leetcode.com/problems/sort-colors/submissions/1103794409/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # lets count frenquency in a harshtable, and the create a new array

        count = {0:0, 1:0, 2:0}
        for num in nums:
            count[num] += 1

        j = 0
        for i in [0, 1, 2]:
            for k in range(0, count[i]):
                nums[j] = i
                j += 1
             

        # for each num, we compare it with the first and last nums element. If it is greatter or equal to the last, we put in the end. If it is smaller, we put in the beggining,.

        # for i in range(0,len(nums)):
        #     if nums[i] > nums[-1]:
        #         # swap the num to the end
        #         aux = nums[-1]
        #         nums[-1] = nums[i]
        #         nums[i] = aux
            
        #     elif nums[i] < nums[0]:
        #         # swap the number to the begginning
        #         aux = nums[0]
        #         nums[0] = nums[i]
        #         nums[i] = aux

        #     elif nums[i] == nums[-1]:
        #         aux = nums[i]
        #         nums.append()

        #     else:
        #         # let the number be in its current position, in the middle
        #         pass

