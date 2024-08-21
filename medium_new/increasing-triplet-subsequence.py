class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75
        # time O(n) space O(1)
        min1, min2 = float('inf'), float('inf')
        for num in nums:
            if num < min1: min1 = num
            elif num != min1 and num < min2: min2 = num
            elif num > min2: return True
        return False


