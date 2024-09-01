class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        # https://leetcode.com/problems/k-th-nearest-obstacle-queries/description/
        import heapq
        heap = []
        res = []
        for i, (x, y) in enumerate(queries):
            queueSize = i-k
            heapq.heappush(heap, -((abs(x)+abs(y))))
            if len(heap) > k: heapq.heappop(heap)
            if len(heap) >= k: res.append(-heap[0])
            else: res.append(-1)
        return res
