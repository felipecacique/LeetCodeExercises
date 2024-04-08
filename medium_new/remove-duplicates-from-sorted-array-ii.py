class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
        k = 0
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[k] and count <= 1:
                nums[k+1] = nums[i]
                k += 1
                count += 1
            elif nums[i] > nums[k]:
                nums[k+1] = nums[i]
                k += 1
                count = 1
        return k + 1