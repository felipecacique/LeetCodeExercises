class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/description/
        memo = {}        
        def dfs(i, lastArr1, lastArr2):
            if i >= len(nums):
                return 1
            count = 0
            for j in range(lastArr1, nums[i]+1):
                k = nums[i] - j  
                if k <= lastArr2:
                    if (i+1,j,k) in memo: c =  memo[(i+1,j,k)]
                    else: c = dfs(i+1, j, k)
                    count += c

            memo[(i,lastArr1, lastArr2)] = count

            return count

        return dfs(0, 0, nums[0]) % (10**9 + 7)