class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # https://leetcode.com/problems/sum-of-subarray-minimums/
        # O(n) using monotonic stack and dp. Every item is added once and popped once from the stack.
        # I search for ideas online (use mono stack and dp), also a solution, and the i spent a long time thinking on the problem, and then I  came up with this solution. This code is all mine. It is a difficult problem
        MOD = 10 ** 9 + 7

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

        return (-sumSubarrayMaxs([-x for x in arr])) % MOD
