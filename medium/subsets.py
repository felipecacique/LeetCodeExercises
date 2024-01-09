# https://leetcode.com/problems/subsets/description/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # solution similar to combination-sum problem. We build the solution from buttom-up by adding the nums one by one in the previous subsets list, generating subsets.

        import copy
        
        subsets = [[]]

        for num in nums:
            for i in range(0, len(subsets)):
                new_subset = copy.copy(subsets[i])
                new_subset.append(num)
                subsets.append(new_subset)

        return subsets