class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/sum-of-subarray-ranges/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
        # time O(n^2) space O(1)
        
        # ans = 0
        # for i in range(len(nums)):
        #     maximum, minimum = nums[i], nums[i]
        #     for j in range(i+1, len(nums)):
        #         maximum = max(maximum, nums[j])
        #         minimum = min(minimum, nums[j])
        #         ans += (maximum - minimum)
        # return ans 


        # similar to https://leetcode.com/problems/sum-of-subarray-minimums/ . Solve um-of-subarray-minimums first, and then this problem becomes easy
        # O(n) using monotonic stack and dp. Every item is added once and popped once from the stack.
        # I search for ideas online (use mono stack and dp), also a solution, and the i spent a long time thinking on the problem, and then I  came up with this solution. This code is all mine. It is a difficult problem

        def sumSubarrayMaxs(arr):
           
            arr = [float("inf")] + arr
            decStack = [0]
            dp = 0
            ans = 0
            for i in range(1, len(arr)):
                
                # Lets keep an decreasing monotonic stack - we add the indexes instead of the value, and then we check arr[i]
                if not decStack or arr[i] < arr[decStack[-1]]:
                    # add i to stack
                    dp = dp + (i - decStack[-1]) * arr[i]
                    decStack.append(i) 
                    # print(i,decStack, dp)
                else:
                    # pop elements and add i
                    while arr[i] >= arr[decStack[-1]]:
                        popped = decStack.pop()
                        dp = dp -  (popped - decStack[-1]) * arr[popped] 
                    dp = dp + (i - decStack[-1]) * arr[i]
                    decStack.append(i)
                
                ans += dp
        
            return ans 

        return  sumSubarrayMaxs(nums) - (-sumSubarrayMaxs([-x for x in nums]))


