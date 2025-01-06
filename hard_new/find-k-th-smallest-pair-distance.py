class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # https://leetcode.com/problems/find-k-th-smallest-pair-distance/submissions/1498855288/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
        
        # # using heapq: time nlogn + klog(m+k)  space n+k. It worked but with Memory Limit Exceeded
        # nums.sort()

        # import heapq
        # heap = []
        # seen = set()
        # for i in range(1,len(nums)):
        #     heap.append((nums[i]-nums[i-1], i-1, i))
        #     seen.add((i-1, i))
        # heapq.heapify(heap)


        # for i in range(k):
        #     if not heap:
        #         return None

        #     dist, l, r = heapq.heappop(heap)

        #     if l-1 >= 0 and not (l-1, r) in seen : 
        #         heapq.heappush(heap, ( nums[r] - nums[l-1], l-1, r))
        #         seen.add((l-1, r))
        #     if r+1 < len(nums) and not (l, r+1) in seen :  
        #         heapq.heappush(heap, ( nums[r+1] - nums[l], l, r+1))
        #         seen.add((l, r+1))

        # return dist
        

        # Solution from neetcode https://www.youtube.com/watch?v=bQ-QcFKwsZc . It is a very difficult problem as it invovles using slinding window and binary search in a non obvious way. Have to model the problem diferently to start with.
        # time O(nlogn + nlog(max)) space = o(1)
        nums.sort()

        # We can calculate the number of pairs for a given distance.
        def helper(dist):
            l = 0
            pairs = 0
            for r in range(len(nums)):
                while l < r and nums[r] - nums[l] > dist:
                    l += 1
                pairs += r - l
            return pairs

        # Use binary search. We play with distance -> pairs, until we find pairs == k. Then we return the distance. It words because we know that distance is proportional with the nnumber of pairs
        l, r = 0, max(nums)
        while l < r:
            m = (l+r)//2   
            pairs = helper(m)
            if pairs < k:
                l = m+1
            else:
                r = m
        return r



