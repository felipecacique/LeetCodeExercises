class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        # https://leetcode.com/problems/maximum-number-of-robots-within-budget/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
        # use monotonic queue and monotonic decreasing stack for finding the max O(n)

        from collections import deque
        queue = deque()
        queueDecr = deque()
        sumCosts = 0
        ans = 0

        for i in range(len(chargeTimes)):

            queue.append(i)

            while queueDecr and chargeTimes[queueDecr[-1]] <= chargeTimes[i]: # keeping a monotonic decreasing stack
                queueDecr.pop()
            queueDecr.append(i)

            maxTime = chargeTimes[queueDecr[0]] 
            sumCosts += runningCosts[i]
            totalCost = len(queue) * sumCosts + maxTime

            while queue and totalCost > budget :
                popIndex = queue.popleft()

                while queueDecr and queueDecr[0] <= popIndex:
                    queueDecr.popleft()
                maxTime = chargeTimes[queueDecr[0]] if queueDecr else 0

                sumCosts -= runningCosts[popIndex]
                totalCost = len(queue) * sumCosts + maxTime

            ans = max(ans, len(queue))
            
        return ans



        # use monotonic queue and heap for finding the max O(nlogn)

        # from collections import deque
        # import heapq
        # queue = deque()
        # heap = []
        # sumCosts = 0
        # ans = 0

        # for i in range(len(chargeTimes)):

        #     queue.append(i)
        #     heapq.heappush(heap, (-chargeTimes[i], i))
        #     while heap and queue and heap[0][1] < queue[0]:
        #         heapq.heappop(heap)
        #     maxTime = -heap[0][0]
        #     sumCosts += runningCosts[i]
        #     totalCost = len(queue) * sumCosts + maxTime

        #     while queue and totalCost > budget :
        #         popIndex = queue.popleft()
        #         while heap and queue and heap[0][1] < queue[0]:
        #             heapq.heappop(heap)
        #         maxTime = -heap[0][0] if queue else 0
        #         sumCosts -= runningCosts[popIndex]
        #         totalCost = len(queue) * sumCosts + maxTime

        #     ans = max(ans, len(queue))
            
        # return ans