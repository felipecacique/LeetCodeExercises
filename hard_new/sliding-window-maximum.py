class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # https://leetcode.com/problems/sliding-window-maximum/?envType=study-plan-v2&envId=top-100-liked
        # o(nlogn) o(n)
        
        import heapq
        heap = []
        output = []

        for i in range(len(nums)):
            num = nums[i]
            heapq.heappush(heap, (-num, i))

            while heap[0][1] <= i-k:
                n, idx = heapq.heappop(heap)
            
            if i >= k-1: 
                n, idx = heap[0]
                output.append(-n)

        return output


