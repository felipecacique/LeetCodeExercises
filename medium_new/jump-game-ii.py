class Solution:
    def jump(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
        # time complexity O(n)
        jumps = 0
        i = 0
        prev_i = i
        while i < len(nums) - 1:
            jumps += 1
            jump_max = float("-inf")
            jump_j = 0

            if i + nums[i] >= len(nums) - 1:
                break

            for j in range(prev_i+1, min(i+nums[i]+1, len(nums))):
                if j + nums[j] > jump_max:
                    jump_max = j + nums[j]
                    jump_j = j
            prev_i = i
            i = jump_j

        return jumps