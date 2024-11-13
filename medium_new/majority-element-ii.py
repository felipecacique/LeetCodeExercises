class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # https://leetcode.com/problems/majority-element-ii/
        n = len(nums)
        harsh = {}
        for num in nums:
            if not num in harsh: harsh[num] = 0
            harsh[num] += 1
        
        ans = []
        for num, count in harsh.items():
            if count / n > 1/3:
                ans.append(num)
        return ans