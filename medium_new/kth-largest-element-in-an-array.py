class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1214948732/?envType=study-plan-v2&envId=leetcode-75
        
        # nums = sorted(nums)
        # return nums[-k]

        # import heapq
        # heapq.heapify(nums)
        # return heapq.nlargest(k, nums)[-1]

        nums = [-n for n in nums]
        print(nums)
        import heapq
        heapq.heapify(nums)
        for _ in range(k):
            largest = -heapq.heappop(nums)
        return largest