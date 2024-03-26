class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75
        # slide window problem

        a = 0
        b = k - 1
 
        average = sum(nums[a:b+1])/k
        maxAverage = average

        while b < len(nums)-1:
            # sliede window to the right
            average = average - nums[a]/k + nums[b+1]/k
            a += 1
            b += 1

            if average > maxAverage:
                maxAverage = average
        
        return maxAverage