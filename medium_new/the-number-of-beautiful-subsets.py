class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # https://leetcode.com/problems/the-number-of-beautiful-subsets/
        # solution got from https://www.youtube.com/watch?v=xNRavrSTUHY&ab_channel=AlgorithmsCasts
        # i understood the solution and replicated it

        self.count = 0
        cannot_visit = [0] * len(nums)

        def dfs(idx):

            if idx >= len(nums):
                self.count += 1
                return
            
            if cannot_visit[nums[idx]] == 0:
                cannot_visit[nums[idx] + k] += 1 # nums[idx] + k is illegal, so we can mark as visited
                cannot_visit[nums[idx] - k] += 1 # nums[idx] - k is illegal, so we can mark as visited
                dfs(idx+1) # situation in which we visit idx
                cannot_visit[nums[idx] + k] -= 1 
                cannot_visit[nums[idx] - k] -= 1
            
            dfs(idx+1) # situation in which we do not visit idx

        cannot_visit = [0] * 2002
        dfs(0)

        return self.count - 1