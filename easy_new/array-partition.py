class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # agrupar maior com maior
        # O(nlogn) to sort it
        ans = 0
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if i%2 == 1:
                ans += nums[i]
        return ans