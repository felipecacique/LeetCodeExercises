class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # https://leetcode.com/problems/next-permutation/description/?envType=study-plan-v2&envId=top-100-liked
        # o(n) o(n)
        exchanged = False
        maxNum = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                idx = nums[i+1]
                for j in range(i+1, len(nums)):
                    if nums[j] <= nums[i]:
                        break
                    idx = j
                nums[i], nums[idx] = nums[idx], nums[i]
                nums[i+1:] = reversed(nums[i+1:])
                exchanged = True
                break
        
        if not exchanged:
            nums.reverse()
            
