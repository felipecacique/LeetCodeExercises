# https://leetcode.com/problems/two-sum/submissions/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time O(n^2) space O(1) - Iterate the list twice
        def Solution1():
            for i, a in enumerate(nums):
                for j, b in enumerate(nums[i + 1 :]):
                    if a + b == target:
                        return [i, j + i + 1]

        # time O(n) space O(n) - Iterate the list once and use hashtable to store the values
        def Solution2():
            h = {}
            for i, a in enumerate(nums):
                # a + b = target
                b = target - a

                # check if b exists in the hashtable
                if b in h:
                    return [i, h[b]]

                # Add the pairs a and i to the hashtable
                h[a] = i

        return Solution2()
