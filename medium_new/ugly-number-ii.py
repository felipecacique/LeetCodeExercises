class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # https://leetcode.com/problems/ugly-number-ii/
        # works but slow implementation
        import heapq
        heap = set([1])
        nums = set([1])
        for i in range(1, n+1):
            newNums = set([])
            numsList = list(nums)
            for j in range(len(numsList)):
                for k in [2, 3, 5]:
                    newNums.add(numsList[j] * k)
                    heap.add(numsList[j] * k)
            nums = newNums
            if len(heap) >= 3.5*n: break

        heap = list(heap)
        heap.sort()
        return heap[n-1]
        heapq.heapify(heap)
        
        ans = 1
        for i in range(n):
            ans = heapq.heappop(heap)
        
        return ans
        