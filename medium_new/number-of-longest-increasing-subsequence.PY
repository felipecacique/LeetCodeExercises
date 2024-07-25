class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # use dynamic programming such as to find the longest increasing subsequence problem. We store the values of the subsequence sizes,and also the number of subsequences that have lead to a string of that size.
        # tome complexity O(n*n)
        # i think there is a faster solution (nlogn) but I wong go for that
        nums.append(inf)
        harsh = [1] * len(nums)
        harshCount = [0] * len(nums)
        for i in range(len(nums)):
            aux = []
            for j in range(i+1):
                # we "add" nums[i] to all previous subsequences of size = harsh[j]. Also store the number of subsequences that lead to that sequence size.
                if nums[i] > nums[j]: 
                    aux.append((harsh[j], harshCount[j])) # saves the subsequence size and the count

            if aux: maxSeqSize, _ = max(aux)
            else: maxSeqSize, _ = 0, 1
            harsh[i] = maxSeqSize + 1

            for seqSize, count in aux:
                if seqSize == maxSeqSize:
                    harshCount[i] += count
            harshCount[i] = max(harshCount[i], 1)

        return harshCount[-1]
         
# SOLUTION OF FINDING THE Longest Increasing Subsequence
# class Solution:
#     def findNumberOfLIS(self, nums: List[int]) -> int:
#         # use dynamic programming such as to find the longest increasing subsequence problem. We store the values of the subsequence sizes, get the longest size and count how many times it has appeared
#         # tome complexity O(n*n)
#         # there is a faster solution (nlogn) but I wong go for that

#         harsh = [1] * len(nums)
#         for i in range(len(nums)):
#             for j in range(i+1):
#                 if nums[i] > nums[j]: 
#                     harsh[i] = max(harsh[i], harsh[j]+1)
#                     print(harsh[i])
#         print(harsh)
#         maxSeqSize = max(harsh)
#         return harsh.count(maxSeqSize)