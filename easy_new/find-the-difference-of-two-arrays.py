class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # https://leetcode.com/problems/find-the-difference-of-two-arrays/submissions/1214017210/?envType=study-plan-v2&envId=leetcode-75

        set1 = set(nums1)
        set2 = set(nums2)

        ans1 = set()
        ans2 = set()

        for n in nums1:
            if n not in set2:
               ans1.add(n)
        
        for n in nums2:
            if n not in set1:
                ans2.add(n)

        return [ans1, ans2]