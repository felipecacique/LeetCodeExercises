import heapq
class MedianFinder:
    # https://leetcode.com/problems/find-median-from-data-stream/description/?envType=study-plan-v2&envId=top-interview-150
    # use 2 heaps. They must be the kept the same size, and the all th evalues of th eheap1 is smaller than heap2. Ao when we pop the higuest of the heap1 and the smallest of the heap2, we found the median. Cyz this is in the middle. 
    def __init__(self):
        self.heap1 = []
        self.heap2 = []

    def addNum(self, num: int) -> None:
        # the heaps must be kept the same size (or +1 in case of even size)
        heap1 = self.heap1
        heap2 = self.heap2
        heap1Largest = -heap1[0] if heap1 else float("-inf")
        heap2Smallest = heap2[0] if heap2 else float("inf")

        if len(heap1) < len(heap2):
            if num <= heap2Smallest:
                heapq.heappush(heap1, -num)
            else:
                aux = heapq.heappop(heap2)
                heapq.heappush(heap1, -aux)
                heapq.heappush(heap2, num)
        elif len(heap1) > len(heap2):
            if num >= heap1Largest:
                heapq.heappush(heap2, num)
            else:
                aux = heapq.heappop(heap1)
                heapq.heappush(heap2, -aux)
                heapq.heappush(heap1, -num)  
        else: # len(heap1) == len(heap2)
            if num <= heap2Smallest:
                heapq.heappush(heap1, -num)
            else:
                heapq.heappush(heap2, num)
        return

    def findMedian(self) -> float:
        heap1 = self.heap1
        heap2 = self.heap2
        if not heap1 and not heap2: return None
        elif len(heap1) > len(heap2): return -heap1[0]
        elif len(heap1) < len(heap2): return heap2[0]
        else: return (-heap1[0] + heap2[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()