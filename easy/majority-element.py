# https://leetcode.com/problems/majority-element/description/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        harsh = {}
        max_count = 0
        max_num = 0

        for num in nums:
            if not num in harsh:
                harsh[num] = 1
            else:
                harsh[num] += 1

            if harsh[num] > max_count:
                max_count = harsh[num]
                max_num = num

        return max_num
