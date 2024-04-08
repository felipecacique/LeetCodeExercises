class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # https://leetcode.com/problems/merge-sorted-array/submissions/1226954901/?envType=study-plan-v2&envId=top-interview-150
        
        arr = []
        i, j = 0, 0
        while i + j < m + n:
            if j >= n or i < m and nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1    

        for i in range(m+n):
            nums1[i] = arr[i]
