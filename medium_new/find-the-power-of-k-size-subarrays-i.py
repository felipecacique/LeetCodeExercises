class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/
        from collections import deque
        queue = deque()
        count = 0
        output = []
        for num in nums:
            
            if not queue or (queue and num == queue[-1]+1): count += 1
            queue.append(num)

            if len(queue) >= k:
                if count == k: output.append(queue[-1])
                else: output.append(-1)
                
                popped = queue.popleft()
                if queue and queue[0] == popped+1: count -= 1
                if not queue: count = 0
            

        return output
        