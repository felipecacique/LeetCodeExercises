#IT IS GIVING TIME LIMIT EXCEEDED
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/description/
        multiplier = multiplier % (10**9 + 7)
 
        import heapq
        numIndex = []
        for i in range(len(nums)):
            numIndex.append((nums[i], i))
        heapq.heapify(numIndex)

        for i in range(k):
            minVal, i = heapq.heappop(numIndex)
            nums[i] = (nums[i] * multiplier) % (10**9 + 7)
            heapq.heappush(numIndex, (nums[i], i))
        
        return nums