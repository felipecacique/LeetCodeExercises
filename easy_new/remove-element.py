class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
        k = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k 