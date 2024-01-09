# https://leetcode.com/problems/product-of-array-except-self/submissions/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # solution 1: 2 two for loops. the first one we get all values left of i and cumpute prodLeft(i) for i in m, answer will be answer[i] = prodLeft(i). Thats is already part of the solution.And what about the values in the right of i? we do the same, but iterating now from the end of the nums list. Calculate the prodRight(i) and multiply it to the answer[i], which is the prodLeft(i). Now answer[i] = prodLeft(i) * prodRight(i). This can be done with a single travel in the both array, since, for example, prodLeft(i) = productLeft(i-1) * nums(i-1). time O(n) space O(n)

        answer = [1] * len(nums)

        # calculate the left product
        prodLeft = 1
        for i in range(1, len(nums)):
            prodLeft = prodLeft * nums[i - 1]
            answer[i] = prodLeft

        # calculate the right product, by iterating backwards, and multiply to the left product
        prodRight = 1
        for i in range(len(nums) - 2, -1, -1):
            prodRight = prodRight * nums[i + 1]
            answer[i] *= prodRight

        return answer
