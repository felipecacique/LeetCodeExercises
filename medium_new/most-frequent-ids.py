class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        # https://leetcode.com/problems/most-frequent-ids/submissions/1350415687/
        # not o(n**2). we improve this to o(nlog) using heap
        output = []
        collection = {}
        import heapq
        heap = []
        for i in range(len(nums)):
            collection[nums[i]] = collection.get(nums[i], 0) + freq[i]
            
            heapq.heappush(heap, (-collection[nums[i]], nums[i]) )

            maxFreq = 0
            while heapq:
                f, n = heapq.heappop(heap)  
                f = -f
                if collection[n] == f: # the values mach so we can consider this value, othersise we just discharge f and n because is must be an old value. Of example, the frequency of 5 was 10. And this was inserted in the heap preciously. But the frequency of 5 was decreased to 7 and also inserted im the heap. So we compare wjat we pop with wuat is the current values in collection. 
                    maxFreq = f
                    heapq.heappush(heap, (-f, n) ) # lets put it back
                    break

            output.append(maxFreq)

            # maxFreq = max(maxFreq, collection[nums[i]])

            # maxFreq = 0
            # for num, f in collection.items():
            #     maxFreq = max(maxFreq, f)

            # output.append(maxFreq)
        return output