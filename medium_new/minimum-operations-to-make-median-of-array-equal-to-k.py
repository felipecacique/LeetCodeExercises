class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        # 2, 5, 5, 6, 8
        # 2, 4, 4, 6, 8
        # time is O(nlogn)
        # https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/
        nums = sorted(nums)
        n = len(nums)
        count = 0


        # if n%2 == 1:   # it is odd
        middleIndex = n//2 
        # else:
        #     abs(k-nums[n//2])
        #     abs(k-nums[n//2-1]

        middle = nums[middleIndex]
        count += abs(middle - k) # we made the middle value becomes equal to k. Now we must change the right and left values in order to keep middle as our median 
        
        # if someone in the right is smaller than middle -> k , then we make it become equal to k
        for i in range(middleIndex+1, n):
            if nums[i] <= k: 
                count += k - nums[i]
            else:
                break

        # similar idea for the left side
        for i in range(middleIndex-1, -1, -1):
            if nums[i] >= k: 
                count += nums[i] - k
            else:
                break            
    
        return count