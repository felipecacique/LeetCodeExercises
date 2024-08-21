class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # https://leetcode.com/problems/total-cost-to-hire-k-workers/?envType=study-plan-v2&envId=leetcode-75
        # O(nlogn)
        
        total_cost = 0

        import heapq
        heap = []
        l, r = 0, len(costs) - 1
        l_limit, r_limit = candidates, r - candidates

        for _ in range(k):
            while l <= r and l < l_limit:
                heapq.heappush(heap, (costs[l], l))
                l += 1
            while l <= r and r > r_limit:
                heapq.heappush(heap, (costs[r], r))
                r -= 1
            
            lowest_worker, index_lowest_worker = heapq.heappop(heap)
            total_cost += lowest_worker

            if index_lowest_worker <= l_limit: l_limit += 1
            elif index_lowest_worker >= r_limit: r_limit -= 1
            
        return total_cost

