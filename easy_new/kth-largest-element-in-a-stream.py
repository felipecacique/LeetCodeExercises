import heapq
class KthLargest:
    # https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums = sorted(nums, reverse=True)
        self.heapKLargest = nums[:k] # min heap that contains the k largest elements
        self.heapSmallest = [-num for num in nums[k:]] # max heap that contains the n-k smallest elements
        heapq.heapify(self.heapKLargest)
        heapq.heapify(self.heapSmallest)
        
    def add(self, val: int) -> int:
        # Add the val to the heap (always keep the size of heapKLargest equal to k)
        if len(self.heapKLargest) < self.k:
            heapq.heappush(self.heapKLargest, val)
        elif val > self.heapKLargest[0]: # smallest from the self.heapKLargest
            smallestFromHeapKLargest = heapq.heappop(self.heapKLargest)
            heapq.heappush(self.heapSmallest, -smallestFromHeapKLargest)
            heapq.heappush(self.heapKLargest, val)
        else:
            heapq.heappush(self.heapSmallest, -val)
        return self.heapKLargest[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)