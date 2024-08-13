# this is my original solution. it works fine. But there is faster solution next
# class Solution:
#     def maximumLength(self, nums: List[int], k: int) -> int:
#         # https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/
#         # same idea of the other solutio, but with a simplification that result in a romotion of one of the fors, since we use a harsh table.
#         # complexity O(n*k)
        
#         numsMods = [n % k for n in nums]

#         from collections import defaultdict
#         harsh = defaultdict(int)

#         for n in numsMods:
#             for c in range(k):
#                 if (c,n) in harsh: harsh[(n,c)] = harsh[(c,n)] + 1 # continue a sequence that started with c and found n (second value); Invert the key pairs, because we are computing a sequence of alternating pairs.
#                 elif (n,c) not in harsh: harsh[(n,c)] = 1 # start a new sequence where the first value is n and next is intended to be c
        
#         return max(harsh.values())



# from a submission's solution. It is the same thing  as my solution above, but using arr instead of harsh tables. It looks cleaner nad easier to understand.
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/
        # same idea of the other solutio, but with a simplification that result in a romotion of one of the fors, since we use a harsh table.
        # complexity O(n*k)
        
        dp = [[0]*k for _ in range(k)]

        for x in nums:
            x = x % k
            for y in range(k):
                dp[y][x] = dp[x][y] + 1

        return max([max(row) for row in dp])


# class Solution:
#     def maximumLength(self, nums: List[int], k: int) -> int:
#         # similar to the other exercise find-the-maximum-length-of-valid-subsequence-i, but expandes for any value of k
#         # we take the mods of all numbers. Now the soluitins will have all with the same mod number or alternating. But what i mean by that is that we take the complement c = (k-1) - m, where m is the mod of a number, and get m then c then m then c. Example, for m = 0 and k = 2. C = (2-1) - 0 = 1.  Initailly we look for 0, then for 1, then for 0, then for 1. Now for m = 1, c = (2-1) - 1 = 0, We initially look for 1, then 0, then 1 ... actually i was wrong about the c. Ccan also assume any value ... So we have to do a for loop for c as well.
#         # complexity O(n*k*k) to slow
        
#         numsMods = [n % k for n in nums]
        
#         counts = []
#         for m in range(k):
#             for c in range(k):
#                 cond = m
#                 count = 0
#                 for n in numsMods:
#                     if n == cond:
#                         count += 1
#                         cond = c if cond == m else m
#                 counts.append(count)
        
#         return max(counts)