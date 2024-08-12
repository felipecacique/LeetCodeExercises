class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
        less = []
        equal = []
        greater = []
        for n in nums:
            if n < pivot:
                less.append(n)
            elif n == pivot:
                equal.append(n)
            else:
                greater.append(n)
        return less + equal + greater