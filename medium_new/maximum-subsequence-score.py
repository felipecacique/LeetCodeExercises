import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # https://leetcode.com/problems/maximum-subsequence-score/?envType=study-plan-v2&envId=leetcode-75
        def Solution1(nums1, nums2, k): # it works for some cases, but not all O(n**2)
            # removing zeroes
            nums1_aux, nums2_aux = [], []
            for i in range(len(nums1)): # remove zeroes
                if nums2[i] != 0:
                    nums1_aux.append(nums1[i])
                    nums2_aux.append(nums2[i])
            nums1, nums2 = nums1_aux, nums2_aux
            if len(nums2) < k : return 0

            # the algorithm starts here
            score = sum(nums1) * min(nums2)
            nums2_heap = [ (nums2[i], i) for i in range(len(nums2)) ]

            # check if we remove element by element, and drop the one that make our score worse 
            while len(nums2_heap) > k:
                heapq.heapify(nums2_heap)
                max_score, remove_i = float('-inf'), None
                nums2_min, nums2_second_min = nums2_heap[0][0], heapq.nsmallest(2,nums2_heap)[1][0]
                
                for j in range(len(nums2_heap)):
                    num2, i = nums2_heap[j]
                    # recalculate the score without i
                    if num2 < nums2_second_min: new_score = (score / num2 - nums1[i]) * nums2_second_min # if the num2 is smaller than the secon min, then as removing it we will change the min. In this situation we have to calculate the score a bit different
                    else: new_score = score - (nums1[i]*nums2_min) # remove ith from the score
                    
                    if new_score > max_score: max_score, remove_i = new_score, i # we must drop the i that improve the score the most

                # put all back to the heap, but remove_i
                nums2_heap = [(num2, i) for num2, i in nums2_heap if i != remove_i]
                score = max_score
            
            return int(score)

        def Solution2(nums1, nums2, k):
            # based on neetcode solution https://www.youtube.com/watch?v=ax1DKi5lJwk   O(nlogn)
            # i tried to replicate by memory
            pairs = [(num1, num2) for num1, num2 in zip(nums1, nums2)]
            pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

            maxScore = float('-inf')
            heap = []
            n1Sum = 0

            for n1, n2 in pairs:
                n1Sum += n1
                heapq.heappush(heap, n1)

                if len(heap) > k:
                    n1Pop = heapq.heappop(heap) # we must pop the one with smaller n1
                    n1Sum -= n1Pop
                if len(heap) == k:
                    maxScore = max(maxScore, n1Sum*n2)

            return maxScore

        return Solution2(nums1, nums2, k)
            
