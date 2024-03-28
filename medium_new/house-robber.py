class Solution:
    def rob(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=leetcode-75
        # nums = [2,7,9,3,1,5,7,33,2,6,34,]
        # look at ith 33. i we add 33 then our amount is best_amount(ith-2), in orther words [2,7,9,3,1,5]. We do not pick the number 7 because of the restriction
        # always keep 2 best solutions, 1 considering ith, and another withou ith. 

        bestAmmountPrevIncluded = 0
        bestAmmountPrevNotIncluded = 0

        for i in range(len(nums)):
            # showld we add numns[i] to the final solution?
            if (nums[i] + bestAmmountPrevNotIncluded) > bestAmmountPrevIncluded: # we compare a situation where we include nums[i] in the solution, or the on that nums[i] is not included
                # keep storing the path where nums[i] will not be included but nums[i-1] is
                bestAmmountPrevIncluded, bestAmmountPrevNotIncluded = nums[i] + bestAmmountPrevNotIncluded, bestAmmountPrevIncluded # we included nums[i]
            else:
                bestAmmountPrevNotIncluded = bestAmmountPrevIncluded
                # bestAmmountPrevIncluded = bestAmmountPrevIncluded
            
        return max(bestAmmountPrevNotIncluded, bestAmmountPrevIncluded)

