class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # https://leetcode.com/problems/median-of-two-sorted-arrays/?envType=study-plan-v2&envId=top-interview-150
        # inspired on the neetcode's solution. I had to copy some parts from neetcode .... 

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        left1, right1 = 0, len(nums1)-1

        while True:
            middle1 = (left1+right1)//2
            middle2 = (m+n)//2 - middle1 - 2 # Apply property (total left == total right)
            print(middle2, middle1, (m+n)//2, nums2)
            # break
            a1 = nums1[middle1] if middle1 >= 0 else float("-inf")
            b1 = nums1[middle1+1] if middle1+1 < m else float("inf")
            a2 = nums2[middle2] if middle2 >= 0 else float("-inf")
            b2 = nums2[middle2+1] if middle2+1 < n else float("inf")
            print("r", a1, b1, a2, b2)
            # Check if the slice at middle2 is valid (all values on the left are greater than all values on the right)
            # if max(a1,a2) <= min(b1,b2):
            if a1 <= b2 and a2 <= b1:
                print("v", a1, b1, a2, b2)
                # it is valid, so we have found the meddle
                # if m + n % 2 == 1: # odd
                #     return max(a1,a2)
                # else: # even
                #     if m % 2 == 1: # both arr are odd
                #         return (a1+a2)/2
                #     else: # both are even
                #         return (max(a1,a2)+min(b1,b2))//2

                if (m + n) % 2: # odd
                    return min(b1,b2)
                else: # even
                    return (max(a1,a2)+min(b1,b2))/2

            else:
                if a1 > b2:
                    right1 = middle1 - 1
                else:
                    left1 = middle1 + 1
        return 0
            
    


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         # lets suppose we found the median m, the total ammount of numbers on the left (considering both arrays) must be the same as the total ammount on the right. With that rule, we are going to guide out binary search, with pointers to both arrays 

#         left1, right1 = 0, len(nums1)-1
#         left2, right2 = 0, len(nums2)-1

#         while left1 <= right1:
#             middle1 = (left1+right1)//2
            
#             # Find the middle1 in the nums2 doing a binary search on nums2
#             while left2 <= right2:
#                 middle2 = (left2+right2)//2
#                 if nums1[middle1] >= nums2[middle2]: left2 = middle2
#                 else: right2 = middle2 - 1
#             # print(middle2)
#             # break
#             totalRight = (len(nums2) - middle2) + (len(nums1) - middle1)
#             totalLeft = middle2 + middle1 - 2
#             if totalRight == totalLeft:
#                 # We found the median
#                 break
#             elif totalRight > totalLeft:
#                 # the median must be mode on the right
#                 left1 = middle1 + 1
#                 right2 = len(nums2)-1
#             else:
#                 right1 = middle1 - 1
#                 left2 = 0

#         return nums1[middle1]