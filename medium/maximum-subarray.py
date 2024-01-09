# https://leetcode.com/problems/maximum-subarray/submissions/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # we travel the array computing the largest local sequences, with sum given by s. When adding a new number num to the sequence, we have 2 options: add num to the previous sequence, or start a new sequence from num. We will chose the option in wich the sum s is greatter. We also have a variable max_sum to store the max value found for the sequences.

        max_sum = nums[0]
        s = nums[0]  # max local sequence sum
        for num in nums[1:]:
            if s + num > num:
                s = s + num
            else:
                s = num
            if s > max_sum:
                max_sum = s
        return max_sum
