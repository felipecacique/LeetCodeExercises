class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/
        # using heap O(nlogn)

        import heapq
        intervals.sort()
        
        groupIntervals = []

        for interval in intervals:
            start, end = interval[0], interval[1]
            if not groupIntervals or start <= groupIntervals[0]: # overlaps with the min, then overlaps with all others, so we have to create a new interval
                heapq.heappush(groupIntervals, end)
                continue
           
            _ = heapq.heappop(groupIntervals)
            heapq.heappush(groupIntervals, end)
        
        return len(groupIntervals)
