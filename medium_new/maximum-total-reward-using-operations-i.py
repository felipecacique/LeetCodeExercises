class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        # https://leetcode.com/problems/maximum-total-reward-using-operations-i/description/
        # combination with prunning based on https://www.youtube.com/watch?v=Rhi6RGJKBFY
        # since we use a set(), the partial solutions (candidates) x will range from 0 to 2000. That way, since we loop the condidates n times, we have the time complexity as 0(n^2)
        # amazing!!
        rewardValues = sorted(rewardValues)
        candidates = set([0])
        for r in rewardValues:
            for x in candidates.copy():
                if r > x: 
                    candidates.add(x+r)
        return max(candidates)

        # rewardValues = sorted(rewardValues)
        # candidates = [0]
        # for r in rewardValues:
        #     for x in candidates.copy():
        #         if r > x: 
        #             candidates.append(x+r)
        # return max(candidates)

# this solution did not work :(
# class Solution:
#     def maxTotalReward(self, rewardValues: List[int]) -> int:
#         # O(n^2) using dinamic programming similar to the longgest increasing subsequence problem if we sort the rewardValues
#         rewardValues = sorted(rewardValues)
#         print(rewardValues)
#         xs = [0] * len(rewardValues)
#         for i in range(len(rewardValues)):
#             r = rewardValues[i]
#             xs[i] = r
#             for j in range(i):
#                 if r > xs[j]: 
#                     # we can add r to the optimal solution xs[j] in which r > xs[j]
#                     xs[i] = max(xs[i], xs[j] + r) # and we get the max there
#         print(xs)
#         return max(xs)
