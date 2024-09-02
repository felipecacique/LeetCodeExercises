class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/first-missing-positive/?envType=study-plan-v2&envId=top-100-liked
        # o(n) o(1)
        # Transform the nums arr in a set. By pop() and add() simultaneously we dont create extra space
        numsSet = set()
        for i in range(len(nums)-1, -1, -1):
            numsSet.add(nums.pop())

        # Check all numbers from [1, n] in order.The first one that is not in nums is ouw answer 
        for x in range(1, len(numsSet)+2):
            if x not in numsSet:
                return x

        return 1