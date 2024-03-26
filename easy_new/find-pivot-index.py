class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75

        sumLeftRight = [nums[0]] * (len(nums))
        sumRightLeft = [nums[-1]] * (len(nums))

        for i in range(1,len(nums)):
            sumLeftRight[i] = sumLeftRight[i-1] + nums[i]
            sumRightLeft[len(nums)-1-i] = sumRightLeft[len(nums)-i] + nums[len(nums)-1-i]
        
        for i in range(0, len(sumLeftRight)):
            if sumLeftRight[i] == sumRightLeft[i]:
                return i

        return -1
        