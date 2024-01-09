# https://leetcode.com/problems/contains-duplicate/submissions/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # check if the numbe have alreade appeared. We will store the already appeared numbers in a harsh table, so that we have time O(n).

        # harsh = {}

        # for num in nums:
        #     if not num in harsh:
        #         harsh[num] = True
        #     else:
        #         return True
        # return False

        harsh = set()

        for num in nums:
            if not num in harsh:
                harsh.add(num)
            else:
                return True
        return False
