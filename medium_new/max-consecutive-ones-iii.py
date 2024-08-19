class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75
        # time O(n) space O(n)
        from collections import deque
        queue = deque()
        sol = 0
        count = 0
        for num in nums:
            queue.append(num)
            count += num 
            while (len(queue) - count > k):
                count -= queue.popleft()
            sol = max(sol, len(queue))
        return sol

            


        