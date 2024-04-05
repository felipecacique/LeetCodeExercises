class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150
        # i must take an action aiming to reach, ammong all possible cells, that one that con allow me go farther
        # before jumping from ith, evaluate the max index i could reach from ithafter jumping. Then jump to the position in which the inx is max
        def Solution1(): # very efficient, but i will try other solutions even more simple
            if len(nums) == 1: return True
            m = len(nums)
            i = 0
            while i < len(nums):
                if nums[i] >= m - 1: return True
                if nums[i] == 0: return False
                max_jump = 0
                max_candidate = 0
                # evaluate candidates before jumping fron ith
                for j in range(i+1, i+1+nums[i]):
                    idx_reached_from_j = j + nums[j]
                    if idx_reached_from_j >= m - 1:
                        return True # we can reach the end
                    if idx_reached_from_j >= max_jump:
                        max_jump = j + nums[j]
                        max_candidate = j
                i = max_candidate

            return True

        def Solution2():
            pass

        return Solution2()


