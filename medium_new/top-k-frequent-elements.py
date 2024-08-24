class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # https://leetcode.com/problems/top-k-frequent-elements/?envType=study-plan-v2&envId=top-100-liked
        from collections import Counter
        freq = Counter(nums)
        freqNum = []
        for num, freq in freq.items():
            freqNum.append((-freq, num))
        import heapq
        heapq.heapify(freqNum)
        sol = []
        for _ in range(k):
            sol.append(heapq.heappop(freqNum)[1])
        return sol