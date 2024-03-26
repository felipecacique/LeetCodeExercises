class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75
        # sum of 2 values equal to k
        pairs = 0
        countNums = {}
        for n in nums:
            complement = k - n
            if countNums.get(complement,0) > 0:
                countNums[complement] -= 1
                pairs += 1
            else:
                countNums[n] = countNums.get(n,0) + 1
        return pairs