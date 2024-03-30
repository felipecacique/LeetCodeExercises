class Solution:
    # https://leetcode.com/problems/longest-increasing-subsequence/?envType=study-plan-v2&envId=top-interview-150
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [10,9,2,5,1,2,3,7,101,18]
        # a sequence can be represented by s(max, count). 
        # I start computing the first sequence S1. 
        # If I get a number that is greatter to the sequence, i must add it to it. 
        # If i find a number that is smaller than s1_max, this is a new candidate, and I start counting from it a new subsequence S2.
        # If s2_count < s1_count and s2_max >= s1_max, then I can discharge the s2, and keep only the s1. Since s2 is smaller, and s2_max is greatter that s1_max, so the fist sequence is better
        # If s2_count >= s1_count and s2_max < s1_max, then S2 is better (leads to a best subsequence) than S1. Do drop s1. One way of thinking is, we have 2 sequences of same size, but s2_max < s1_max, then we could find a number x that can be added to s2, but cannot be added to s1. So s2 is a better candidate,and we dischange s1
        # will have a list with appended best candididates, and we only have to compare the current candidate to the previous one only. 
        
        def Solution1(): # brute force
            subseqs = [ [nums[0], 1, [nums[0]]] ]# s_max, s_count
            sizeMax = 1
            for i in range(1,len(nums)):
                for j in range(0,len(subseqs)): # we will compute all subsequences
                    if nums[i] > subseqs[j][0]:
                        # add num to my current sequence
                        sizeMax = max(sizeMax, subseqs[j][1] + 1)
                        subseqs.append([nums[i], subseqs[j][1] + 1, subseqs[j][2] + [nums[i]] ])
                    
                if nums[i] < subseqs[-1][0]:
                    # start a new candidate subsequence
                    subseqs.append([nums[i], 1, [nums[i]]])
                
            
                if nums[i] > subseqs[-1][0]:
                    # add num to my previous sequence
                    subseqs[-1][0], subseqs[-1][1] = nums[i], subseqs[-1][1] + 1
                    subseqs[-1][2].append(nums[i])
                    sizeMax = max(sizeMax, subseqs[-1][1])

                # # remove the bad candidates (speed up the code)
                # new = []
                # for j in range(len(subseqs)-1, 1, -1):
                #     if subseqs[j][0] < subseqs[j-1][0] and subseqs[j][1] >= subseqs[j-1][1]:
                #         # s is a better candidate than subseqs[-1], so we can remove subseqs[-1]
                #         subseqs.pop()
                #     else:
                #         new.append(subseqs)

                # for j in range(len(subseqs)-1, 1, -1):
                #     if subseqs[j][0] > subseqs[j-1][0] and subseqs[j][1] <= subseqs[j-1][1]:
                #         # subseqs[-1] is a better candidate than s, so we can remove s and contiue working with our prev subsequence subseqs[-1]
                #         s = subseqs.pop()
                #     else: 
                
            return sizeMax

        
        def Solution2():
            # solution from https://www.youtube.com/watch?v=0wT67DOzqBg&list=FLuLnbXnMa2w0iSGACDOkJDw&index=1&t=7s&pp=gAQB
            # dynamic programing O(n^2). We will compute buttom up the largest sequence in which ith is in, which we will store in dp(ith). 
            # dp(ith) is a function of the previous largests sequences already stored. 
            # For ith, we look at all sequences sizes in wich the other nums is in. 
            # We will add ith to the largest sequence that it can be added,
            # so we get all sequences in which ith can be in (ith > previous) and get the maximum and sum 1. 
            # If ith <= previous we start a new sequence from it, of size 1. 
            # At the end of the allgorithm, we pick up the larggest sequence by getting the max value


            largestSequenceWithNumIncluded = [1] * len(nums)
            for i in range(1, len(nums)):
                for j in range(i):
                    if nums[i] > nums[j]: # so we can add i to the largest subsequence that j is in
                        # but we will pick the max subsequence in which i can be added 
                        largestSequenceWithNumIncluded[i] = max(largestSequenceWithNumIncluded[j]+1, largestSequenceWithNumIncluded[i])
            return max(largestSequenceWithNumIncluded)

        def Solution3():
            # solution from https://www.youtube.com/watch?v=Xq3hlMvhrkE&list=FLuLnbXnMa2w0iSGACDOkJDw&index=3&t=6s&ab_channel=NikhilLohia
            # O(nlogn) inspired in the patience game, where we have to minimize the number of piles, and the optimum number of piles is our longest sequence

            pile = [nums[0]]

            for num in nums[1:]:
                added = False
                for j, p in enumerate(pile):
                    if num <= p:
                        pile[j] = num
                        added = True
                        break
                if not added:
                    pile.append(num) 
            
            return len(pile)
                    

        return Solution3()









