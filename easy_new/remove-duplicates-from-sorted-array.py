class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1226906748/?envType=study-plan-v2&envId=top-interview-150
        k = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[k]:
                nums[k+1] = nums[i]
                k += 1
        return k + 1