class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # https://leetcode.com/problems/find-k-pairs-with-smallest-sums/?envType=study-plan-v2&envId=top-interview-150
        # we need to get the k smallest elements from nums1 and nums2, so instead of sorting, we use priority queue. Oh, its is already sorted =D
        def Solution1(nums1, nums2, k): # Memory Limit Exceeded
            pairs = []
            count = 0
            visited = set()

            for j in range(min(k,len(nums1))):
                for i in range(min(k,len(nums2))):
                    if (j,i) not in visited:
                        pairs.append( (nums1[j] + nums2[i], [nums1[j], nums2[i]]) ) 
                        visited.add((j,i))
                        count += 1
                # if count>k*2+1:            
                #     break

                count = 0
                for j in range(min(k,len(nums2))):
                    for i in range(min(k,len(nums1))):
                        if (i,j) not in visited:
                            pairs.append( (nums1[i] + nums2[j], [nums1[i], nums2[j]]) )
                            visited.add((i,j))
                            count += 1
                    # if count>k*2+1:            
                    #     break
                
            pairs = sorted(pairs)

            if len(pairs) < k:
                return [ pairs[i][1] for i in range(len(pairs)) ]
            else:
                return [ pairs[i][1] for i in range(k) ]

        def Solution2(nums1, nums2, k): # using heap
            # solution O(klogK)  https://www.youtube.com/watch?v=Youk8DDnLU8&ab_channel=ErraK

            pairs = [(nums1[0]+nums2[0], 0, 0)] # sum, index i, index i
            visited = set((0,0))
            import heapq
            # heapq.heapify(pairs)
            output = []
            while k > 0 and pairs: 
                sum_, i, j = heapq.heappop(pairs) # get the smallest
                output.append([nums1[i],nums2[j]])
                k -= 1
                if j+1 < len(nums2):
                    if not (i, j+1) in visited:
                        heapq.heappush(pairs, (nums1[i]+nums2[j+1], i, j+1) )
                        visited.add( (i, j+1) )
                if i+1 < len(nums1):
                    if not (i+1, j) in visited:
                        heapq.heappush(pairs, (nums1[i+1]+nums2[j], i+1, j) )
                        visited.add( (i+1, j) )
            return output




        return Solution2(nums1, nums2, k)