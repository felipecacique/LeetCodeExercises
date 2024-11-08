class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
        # use monotonic stack or pointers time o(n) space o(n)

        total = 0
        subarray = {} # keep the count of unique elements in the subarray
        ans = 0
        repeated = set() # keep all the repeated elements in the subarray

        j = 0
        for i in range(len(nums)):

            total += nums[i]
            subarray[nums[i]] = subarray.get(nums[i], 0) + 1 # add new elements to the subarray that starts in j and ends in i
            if subarray[nums[i]] > 1:
                repeated.add(nums[i])

            if i - j > k - 1: # keep the window size equal to k
                total -= nums[j]
                subarray[nums[j]] -= 1 
                if nums[j] in repeated and subarray[nums[j]] <= 1:
                    repeated.remove(nums[j])
                j += 1
                
            if i - j == k - 1 and not repeated: # if the window size is equal to k and no repeated elements, then it is a candidate
                ans = max(ans, total)
        
        return ans
