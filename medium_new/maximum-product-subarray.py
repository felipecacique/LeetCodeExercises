class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/maximum-product-subarray/?envType=study-plan-v2&envId=top-100-liked
        # time O(n) space O(1)
        maxPos, minNeg, sol = 1, 1, nums[0]
        for num in nums:
            x = maxPos * num
            y = minNeg * num
            maxPos, minNeg = max(num, x, y), min(num, x, y)
            sol = max(sol, maxPos)
        return sol

        
        # maxPos, minNeg, sol = 1, 1, nums[0]
        # for num in nums:
        #     maxPos, minNeg = max(num, maxPos * num, minNeg * num), min(num, maxPos * num, minNeg * num)
        #     sol = max(sol, maxPos)
        # return sol


        # maxPos = 1
        # minNeg = 1

        # for num in nums:
        #     maxPos = max(maxPos, maxPos * num, minNeg * num)
        #     minNeg = min(maxPos, maxPos * num, minNeg * num)
        
        # return maxPos