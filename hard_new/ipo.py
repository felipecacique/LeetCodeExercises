class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # https://leetcode.com/problems/ipo/?envType=study-plan-v2&envId=top-interview-150
        # sort the arrays by capital needed. Do a for adding the tasks in which we could make (given our amount) to a priority heap. The tasks with more profit will be on the top of the heap. We pop the top one and do this task, add the profit to our capital, and repeat the proccess.
        # time complexity O(nlog) to sort, and add k items to the heap

        profitsCapital = sorted(zip(capital, profits))
        wallet = w
        import heapq
        heap = []
        i = 0
        for j in range(k):
            while i < len(profitsCapital) and profitsCapital[i][0] <= wallet:
                heapq.heappush(heap, -profitsCapital[i][1]) 
                i += 1
            if heap == []: break
            profit = heapq.heappop(heap)
            wallet += -profit
        return wallet


# class Solution:
#     def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
#         # https://leetcode.com/problems/ipo/?envType=study-plan-v2&envId=top-interview-150
#         # sort the arrays by capital needed. Do a for adding the tasks in which we could make (given our amount) to a priority heap. The tasks with more profit will be on the top of the heap. We pop the top one and do this task, add the profit to our capital, and repeat the proccess.
#         # time complexity O(nlog) to sort, and add k items to the heap

#         profitsCapital = sorted(zip(capital, profits))
#         wallet = w
#         import heapq
#         heap = []
#         i = 0
#         for j in range(k):
#             while i < len(profitsCapital):
#                 if profitsCapital[i][0] <= wallet:
#                     heapq.heappush(heap, (-profitsCapital[i][1], profitsCapital[i][0])) # (-profits, capital)
#                 else:
#                     break
#                 i += 1
#             if heap == []:
#                 break
#             profit, capital = heapq.heappop(heap)
#             wallet += -profit
#         return wallet
        