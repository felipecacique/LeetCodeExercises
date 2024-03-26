class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75
        # we will use 2 pointers
        a = 0
        b = 1 # it ill point to the closest number non zero in the right

        while b < len(nums) and a < len(nums):
            if nums[a] == 0:
                
                b = max(a,b)
                # we need to replace the zero with the next number in the right
                while b < len(nums) and nums[b] == 0:
                    # we skip zeroes
                    b += 1

                if b < len(nums):
                    # we found a number, so lets replace it
                    nums[a] = nums[b]
                    nums[b] = 0
            a += 1
        