class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/submissions/1269872013/?envType=daily-question&envId=2024-05-27
        # O(n)
        count = [0] + [0] * len(nums)

        for num in nums:
            if num < len(count):
                count[num] += 1
            else:
                count[-1] += 1

        accum = 0
        for i in range(len(count)-1, -1, -1):
            accum += count[i]
            x = i
            if x == accum:
                return x
        
        return -1
