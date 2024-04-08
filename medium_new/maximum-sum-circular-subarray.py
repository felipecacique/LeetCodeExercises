class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/maximum-sum-circular-subarray/?envType=study-plan-v2&envId=top-interview-150
        # similar to miximum-sum problem. but there is an extra part which is dealing with sequences that loops the array. To calculate the max squence in which nums[0] and nums[-1] is included, we did sum(nums) - min_sequence[1:-2](min sequence between the first and last num) 
        
        max_subarray, min_subarray = float('-inf'), float('inf')
        subarray, subarraymin = 0, 0

        for i in range(len(nums)):
            n = nums[i]
            subarray = subarray + n
            if n >= subarray:
                subarray = n # it is better start a new subarray at n, otherwise we just keep our subarray
            max_subarray = max(max_subarray, subarray)

            if i > 0 and i < len(nums) - 1:    
                subarraymin = subarraymin + n
                if n <= subarraymin:
                    subarraymin = n 
            min_subarray = min(min_subarray, subarraymin)

        return max(max_subarray, sum(nums) - min_subarray) if len(nums) >= 3 else max_subarray

