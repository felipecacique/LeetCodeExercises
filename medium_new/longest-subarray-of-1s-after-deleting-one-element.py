class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75
        # similar to max-consecutive-ones-iii problem. Same solution, but make k == 1
        # time O(n) space O(n)
        k = 1
        from collections import deque
        queue = deque()
        sol = 0
        count = 0
        for num in nums:
            queue.append(num)
            count += num 
            while (len(queue) - count > k):
                count -= queue.popleft()
            sol = max(sol, len(queue)-1)
        return sol

            
