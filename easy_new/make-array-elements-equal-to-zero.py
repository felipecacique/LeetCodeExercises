class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/make-array-elements-equal-to-zero/description/
        ans = 0
        total = sum(nums)
        for i in range(len(nums)):
            if nums[i] == 0: # it is a possible start
                # play the game starting from both directions
                for signal in [-1, 1]: # start to the right, and left
                    total_aux = total
                    nums_aux = nums[:]
                    j = i
                    while j >= 0 and j < len(nums):
                        if nums_aux[j] > 0:
                            signal *= -1
                            nums_aux[j] -= 1
                            total_aux -= 1
                        if total_aux == 0: # all nums are 0, so we completed the game
                            ans += 1
                            break
                        j += signal
        return ans
                
                    
                    

                
            